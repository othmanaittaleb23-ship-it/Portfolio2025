from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='image_src')
def image_src(value):
    """Return a usable image URL for ImageField-like values.

    - If the stored name/value starts with http(s), return it directly.
    - If the value has a .url attribute, return that.
    - Otherwise, build a /media/ path from the stored name.
    """
    if not value:
        return ''

    # value can be an ImageFieldFile or a plain string
    try:
        name = getattr(value, 'name', None) or str(value)
    except Exception:
        try:
            name = str(value)
        except Exception:
            return ''

    name = name or ''

    if name.startswith('http://') or name.startswith('https://'):
        return name

    # If it looks like an absolute path already (starts with /media/), return as-is
    if name.startswith(settings.MEDIA_URL):
        return name

    # If the field provides a .url property (file exists), prefer it
    try:
        url = value.url
        return url
    except Exception:
        pass

    # Fallback: construct a media URL
    return f"{settings.MEDIA_URL.rstrip('/')}/{name.lstrip('/')}"
