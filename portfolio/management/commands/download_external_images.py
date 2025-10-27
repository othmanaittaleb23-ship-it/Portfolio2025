import os
import logging
from urllib.parse import urlsplit, unquote

import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.db import transaction

from portfolio.models import Experience, Education

logger = logging.getLogger(__name__)


def _safe_filename_from_url(url, fallback_prefix):
    path = urlsplit(url).path
    name = os.path.basename(path) or ''
    name = unquote(name)
    if not name:
        name = f"{fallback_prefix}.img"
    return name


class Command(BaseCommand):
    help = 'Télécharge les images externes référencées dans Experience/Education et les sauvegarde dans MEDIA via les ImageFields.'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Ne pas écrire, juste afficher ce qui serait fait')
        parser.add_argument('--timeout', type=int, default=10, help='Timeout réseau en secondes')

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        timeout = options['timeout']

        targets = [
            ('Experience', Experience, 'company_logo'),
            ('Education', Education, 'institution_logo'),
        ]

        total = 0
        updated = 0

        for model_name, Model, field_name in targets:
            self.stdout.write(f"=== Traitement {model_name}.{field_name} ===")
            qs = Model.objects.all()
            for obj in qs:
                total += 1
                field = getattr(obj, field_name)
                # field can be an ImageFieldFile; its .name may contain an external URL if old fixtures saved it
                name = getattr(field, 'name', None)
                if not name:
                    continue

                if not (name.startswith('http://') or name.startswith('https://')):
                    # already a local media path
                    continue

                self.stdout.write(f"Found external image for {model_name} pk={obj.pk}: {name}")

                if dry_run:
                    continue

                try:
                    resp = requests.get(name, timeout=timeout)
                    resp.raise_for_status()
                except Exception as e:
                    logger.warning("Failed to download %s: %s", name, e)
                    self.stdout.write(self.style.WARNING(f"  -> failed to download: {e}"))
                    continue

                filename = _safe_filename_from_url(name, f"{model_name}_{obj.pk}")
                # Ensure unique-ish filename by prefixing with model and pk
                filename = f"{model_name.lower()}_{obj.pk}_{filename}"

                try:
                    with transaction.atomic():
                        field.save(filename, ContentFile(resp.content), save=True)
                        obj.save()
                        updated += 1
                        self.stdout.write(self.style.SUCCESS(f"  -> saved as {field.name}"))
                except Exception as e:
                    logger.exception("Failed to save downloaded image for %s pk=%s", model_name, obj.pk)
                    self.stdout.write(self.style.ERROR(f"  -> failed to save: {e}"))

        self.stdout.write(f"Done. Scanned {total} entries. Updated {updated} images.")
