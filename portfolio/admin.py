from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import About, Project, Skill, Experience, Education, Contact, Certificate, Statistics, SiteSettings

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'profile_preview', 'cv_status', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at', 'profile_image_preview']
    
    fieldsets = (
        ('📝 Informations personnelles', {
            'fields': ('name', 'title', 'description', 'profile_image', 'profile_image_preview')
        }),
        ('📞 Contact', {
            'fields': ('email', 'phone', 'location')
        }),
        ('🌐 Réseaux sociaux', {
            'fields': ('linkedin', 'github', 'website')
        }),
        ('📄 CV', {
            'fields': ('cv',),
            'description': 'Téléchargez votre CV au format PDF'
        }),
        ('🕐 Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def profile_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%; object-fit: cover;" />', obj.profile_image.url)
        return "Aucune image"
    profile_preview.short_description = "Photo"
    
    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="200" style="border-radius: 10px;" />', obj.profile_image.url)
        return "Aucune image téléchargée"
    profile_image_preview.short_description = "Aperçu de la photo"
    
    def cv_status(self, obj):
        if obj.cv:
            return format_html('<span style="color: green;">✓ Disponible</span>')
        return format_html('<span style="color: red;">✗ Manquant</span>')
    cv_status.short_description = "CV"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'video_status', 'is_featured', 'is_active', 'tech_count', 'links_available', 'created_at']
    list_filter = ['is_featured', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['is_featured', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'image_preview_large', 'video_preview']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('💼 Informations du projet', {
            'fields': ('title', 'short_description', 'description', 'image', 'image_preview_large'),
            'description': 'Informations principales du projet'
        }),
        ('🛠️ Technologies et liens', {
            'fields': ('technologies', 'github_url', 'github_url_2', 'live_url'),
            'description': 'Séparez les technologies par des virgules (ex: Django, React, PostgreSQL)'
        }),
        ('🎥 Vidéo de démonstration', {
            'fields': ('demo_video_url', 'demo_video_file', 'video_preview'),
            'description': 'Choisissez une option : URL YouTube/Vimeo OU uploadez un fichier vidéo local'
        }),
        ('⭐ Statut', {
            'fields': ('is_featured', 'is_active'),
            'description': 'Projet en vedette = affiché en premier'
        }),
        ('🕐 Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="border-radius: 5px; object-fit: cover;" />', obj.image.url)
        return "Aucune image"
    image_preview.short_description = "Image"
    
    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="300" style="border-radius: 10px;" />', obj.image.url)
        return "Aucune image téléchargée"
    image_preview_large.short_description = "Aperçu de l'image"
    
    def featured_badge(self, obj):
        if obj.is_featured:
            return format_html('<span style="background: #10b981; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">⭐ EN VEDETTE</span>')
        return "-"
    featured_badge.short_description = "Vedette"
    
    def status_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="background: #10b981; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✓ Actif</span>')
        return format_html('<span style="background: #6b7280; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✗ Inactif</span>')
    status_badge.short_description = "Statut"
    
    def tech_count(self, obj):
        count = len(obj.get_technologies_list())
        return format_html('<span style="background: #374151; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">{} tech</span>', count)
    tech_count.short_description = "Technologies"
    
    def links_available(self, obj):
        links = []
        if obj.github_url:
            links.append('GitHub')
        if obj.github_url_2:
            links.append('GitHub 2')
        if obj.live_url:
            links.append('Demo')
        if links:
            return format_html('<span style="color: #10b981;">✓ {}</span>', ', '.join(links))
        return format_html('<span style="color: #6b7280;">Aucun lien</span>')
    links_available.short_description = "Liens"
    
    def video_status(self, obj):
        if obj.demo_video_file or obj.demo_video_url:
            video_type = "Fichier" if obj.demo_video_file else "URL"
            return format_html('<span style="background: #8b5cf6; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">🎥 {}</span>', video_type)
        return format_html('<span style="color: #6b7280;">-</span>')
    video_status.short_description = "Démo"
    
    def video_preview(self, obj):
        if obj.demo_video_file:
            return format_html(
                '<video width="400" controls style="border-radius: 10px; max-width: 100%;">'
                '<source src="{}" type="video/mp4">'
                'Votre navigateur ne supporte pas la lecture de vidéos.'
                '</video>'
                '<p style="color: #10b981; margin-top: 10px;"><strong>✓ Vidéo uploadée</strong></p>',
                obj.demo_video_file.url
            )
        elif obj.demo_video_url:
            if 'youtube.com' in obj.demo_video_url or 'youtu.be' in obj.demo_video_url:
                embed_url = obj.get_video_embed_url()
                return format_html(
                    '<iframe width="400" height="225" src="{}" frameborder="0" allowfullscreen style="border-radius: 10px;"></iframe>'
                    '<p style="color: #10b981; margin-top: 10px;"><strong>✓ Vidéo YouTube</strong></p>',
                    embed_url
                )
            elif 'vimeo.com' in obj.demo_video_url:
                embed_url = obj.get_video_embed_url()
                return format_html(
                    '<iframe width="400" height="225" src="{}" frameborder="0" allowfullscreen style="border-radius: 10px;"></iframe>'
                    '<p style="color: #10b981; margin-top: 10px;"><strong>✓ Vidéo Vimeo</strong></p>',
                    embed_url
                )
            else:
                return format_html(
                    '<video width="400" controls style="border-radius: 10px; max-width: 100%;">'
                    '<source src="{}" type="video/mp4">'
                    'Votre navigateur ne supporte pas la lecture de vidéos.'
                    '</video>'
                    '<p style="color: #10b981; margin-top: 10px;"><strong>✓ Lien vidéo direct</strong></p>',
                    obj.demo_video_url
                )
        return format_html('<p style="color: #6b7280;">Aucune vidéo configurée</p>')
    video_preview.short_description = "Aperçu de la vidéo"

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_preview', 'category_badge', 'level', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    list_editable = ['level', 'order', 'is_active']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('🎯 Compétence', {
            'fields': ('name', 'category', 'icon'),
            'description': 'Utilisez des classes Font Awesome pour les icônes (ex: fas fa-python)'
        }),
        ('📊 Niveau et ordre', {
            'fields': ('level', 'order', 'is_active'),
            'description': 'Niveau: 0-100, Ordre: plus petit = affiché en premier'
        })
    )
    
    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="{}" style="font-size: 20px; color: #10b981;"></i>', obj.icon)
        return "-"
    icon_preview.short_description = "Icône"
    
    def category_badge(self, obj):
        colors = {
            'programming': '#3b82f6',
            'framework': '#8b5cf6',
            'database': '#f59e0b',
            'tool': '#10b981',
            'other': '#6b7280'
        }
        color = colors.get(obj.category, '#6b7280')
        return format_html('<span style="background: {}; color: white; padding: 3px 10px; border-radius: 5px; font-size: 11px;">{}</span>', color, obj.get_category_display())
    category_badge.short_description = "Catégorie"
    
    def level_bar(self, obj):
        color = '#10b981' if obj.level >= 70 else '#f59e0b' if obj.level >= 40 else '#6b7280'
        return format_html(
            '<div style="width: 100px; background: #e5e7eb; border-radius: 5px; overflow: hidden;">'
            '<div style="width: {}%; background: {}; height: 20px; display: flex; align-items: center; justify-content: center; color: white; font-size: 11px; font-weight: bold;">{}</div>'
            '</div>',
            obj.level, color, f'{obj.level}%'
        )
    level_bar.short_description = "Niveau"
    
    def status_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="color: #10b981;">✓</span>')
        return format_html('<span style="color: #6b7280;">✗</span>')
    status_badge.short_description = "Actif"

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'logo_preview', 'period_display', 'is_current', 'order']
    list_filter = ['is_current', 'start_date']
    search_fields = ['position', 'company']
    list_editable = ['order', 'is_current']
    ordering = ['-order', '-start_date']
    readonly_fields = ['logo_preview_large']
    
    fieldsets = (
        ('💼 Informations professionnelles', {
            'fields': ('company', 'position', 'description', 'company_logo', 'logo_preview_large')
        }),
        ('📅 Période', {
            'fields': ('start_date', 'end_date', 'is_current'),
            'description': 'Cochez "En cours" si vous travaillez actuellement dans cette entreprise'
        }),
        ('🔢 Ordre d\'affichage', {
            'fields': ('order',),
            'description': 'Plus petit = affiché en premier'
        })
    )
    
    def logo_preview(self, obj):
        if obj.company_logo:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 5px; object-fit: contain;" />', obj.company_logo.url)
        return "-"
    logo_preview.short_description = "Logo"
    
    def logo_preview_large(self, obj):
        if obj.company_logo:
            return format_html('<img src="{}" width="150" style="border-radius: 10px;" />', obj.company_logo.url)
        return "Aucun logo téléchargé"
    logo_preview_large.short_description = "Aperçu du logo"
    
    def period_display(self, obj):
        start = obj.start_date.strftime('%m/%Y')
        end = 'Présent' if obj.is_current else obj.end_date.strftime('%m/%Y') if obj.end_date else '-'
        return f"{start} - {end}"
    period_display.short_description = "Période"
    
    def current_badge(self, obj):
        if obj.is_current:
            return format_html('<span style="background: #10b981; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✓ En cours</span>')
        return "-"
    current_badge.short_description = "Statut"

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'start_date']
    search_fields = ['degree', 'institution', 'field_of_study']
    list_editable = ['order', 'is_current']
    ordering = ['-order', '-start_date']
    
    fieldsets = (
        ('Formation', {
            'fields': ('institution', 'degree', 'field_of_study', 'description', 'institution_logo')
        }),
        ('Période', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Ordre d\'affichage', {
            'fields': ('order',)
        })
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message_preview', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    actions = ['mark_as_read', 'mark_as_unread']
    
    fieldsets = (
        ('📧 Message', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('📊 Statut', {
            'fields': ('is_read', 'created_at')
        })
    )
    
    def message_preview(self, obj):
        preview = obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
        return format_html('<span style="color: #6b7280; font-style: italic;">{}</span>', preview)
    message_preview.short_description = "Aperçu"
    
    def read_status(self, obj):
        if obj.is_read:
            return format_html('<span style="background: #10b981; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✓ Lu</span>')
        return format_html('<span style="background: #f59e0b; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">● Non lu</span>')
    read_status.short_description = "Statut"
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} message(s) marqué(s) comme lu(s).')
    mark_as_read.short_description = "Marquer comme lu"
    
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} message(s) marqué(s) comme non lu(s).')
    mark_as_unread.short_description = "Marquer comme non lu"
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'cert_preview', 'issued_date', 'verified', 'is_active', 'order']
    list_filter = ['verified', 'is_active', 'issued_date']
    search_fields = ['title', 'issuer']
    list_editable = ['verified', 'is_active', 'order']
    ordering = ['-issued_date', '-order']
    readonly_fields = ['cert_preview_large']
    date_hierarchy = 'issued_date'

    fieldsets = (
        ('🏆 Certificat', {
            'fields': ('title', 'issuer', 'issued_date', 'file', 'image', 'cert_preview_large', 'credential_url'),
            'description': 'Téléchargez soit un fichier PDF, soit une image du certificat'
        }),
        ('✓ Statut', {
            'fields': ('verified', 'is_active', 'order'),
            'description': 'Vérifié = badge de vérification affiché'
        }),
    )
    
    def cert_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="border-radius: 5px; object-fit: cover;" />', obj.image.url)
        elif obj.file:
            return format_html('<i class="fas fa-file-pdf" style="font-size: 30px; color: #dc2626;"></i>')
        return "-"
    cert_preview.short_description = "Aperçu"
    
    def cert_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="300" style="border-radius: 10px;" />', obj.image.url)
        elif obj.file:
            return format_html('<p>Fichier PDF: <a href="{}" target="_blank">Voir le certificat</a></p>', obj.file.url)
        return "Aucun fichier téléchargé"
    cert_preview_large.short_description = "Aperçu du certificat"
    
    def verified_badge(self, obj):
        if obj.verified:
            return format_html('<span style="background: #10b981; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✓ Vérifié</span>')
        return format_html('<span style="background: #6b7280; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">Non vérifié</span>')
    verified_badge.short_description = "Vérification"
    
    def status_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="color: #10b981;">✓</span>')
        return format_html('<span style="color: #6b7280;">✗</span>')
    status_badge.short_description = "Actif"

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['projects_count', 'years_experience', 'technologies_count', 'satisfaction_rate', 'updated_at']
    readonly_fields = ['updated_at']
    
    fieldsets = (
        ('📊 Statistiques de la page d\'accueil', {
            'fields': ('projects_count', 'years_experience', 'technologies_count', 'satisfaction_rate'),
            'description': 'Ces chiffres sont affichés dans la section statistiques de la page d\'accueil'
        }),
        ('🕐 Dernière mise à jour', {
            'fields': ('updated_at',),
        }),
    )
    
    def has_add_permission(self, request):
        # Empêcher la création de plusieurs instances
        return not Statistics.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Empêcher la suppression
        return False

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['chat_status', 'tawk_to_widget_id', 'updated_at']
    readonly_fields = ['updated_at']
    
    fieldsets = (
        ('💬 Chat en Direct (Tawk.to)', {
            'fields': ('enable_chat', 'tawk_to_widget_id'),
            'description': 'Configurez le widget de chat Tawk.to. Créez un compte sur https://www.tawk.to/ et collez votre ID ici.'
        }),
        ('🕐 Dernière mise à jour', {
            'fields': ('updated_at',),
        }),
    )
    
    def chat_status(self, obj):
        if obj.enable_chat and obj.tawk_to_widget_id:
            return format_html('<span style="background: #10b981; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✓ Actif</span>')
        elif obj.enable_chat and not obj.tawk_to_widget_id:
            return format_html('<span style="background: #f59e0b; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">⚠ ID manquant</span>')
        return format_html('<span style="background: #6b7280; color: white; padding: 3px 8px; border-radius: 5px; font-size: 11px;">✗ Désactivé</span>')
    chat_status.short_description = "Statut du Chat"
    
    def has_add_permission(self, request):
        # Empêcher la création de plusieurs instances
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Empêcher la suppression
        return False

# Configuration de l'admin
admin.site.site_header = "🎨 Portfolio Administration"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Bienvenue dans l'administration de votre portfolio"