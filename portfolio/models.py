from django.db import models
from django.utils import timezone

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Image de profil")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Téléchargez votre CV au format PDF")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('tools', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.IntegerField(default=0, help_text="Skill level from 0 to 100")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Image du projet")
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies used")
    github_url = models.URLField(blank=True)
    github_url_2 = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    demo_video_url = models.URLField(
        blank=True, 
        help_text="URL de la vidéo (YouTube, Vimeo, ou lien direct)"
    )
    demo_video_file = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True,
        help_text="Ou uploadez une vidéo locale (.mp4, .webm, .mov)"
    )
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
    
    def get_demo_video(self):
        """Retourne l'URL ou le fichier de la vidéo de démonstration"""
        if self.demo_video_file:
            return self.demo_video_file.url
        return self.demo_video_url
    
    def get_video_embed_url(self):
        """Convertit l'URL de la vidéo en URL embed pour YouTube/Vimeo"""
        video_source = self.get_demo_video()
        if not video_source:
            return None
        
        # YouTube
        if 'youtube.com' in video_source or 'youtu.be' in video_source:
            if 'youtu.be/' in video_source:
                video_id = video_source.split('youtu.be/')[1].split('?')[0]
            else:
                video_id = video_source.split('v=')[1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        
        # Vimeo
        elif 'vimeo.com' in video_source:
            video_id = video_source.split('vimeo.com/')[1].split('?')[0]
            return f'https://player.vimeo.com/video/{video_id}'
        
        # Lien direct (mp4, etc.) ou fichier uploadé
        else:
            return video_source

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to='companies/', blank=True, null=True, help_text="Logo de l'entreprise")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', '-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    institution_logo = models.ImageField(upload_to='institutions/', blank=True, null=True, help_text="Logo de l'institution")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', '-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Certificate(models.Model):
    """Représente un certificat / formation courte avec image et statut vérifié."""
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    # Support both an uploaded file (PDF) and an optional image thumbnail.
    file = models.FileField(upload_to='certificates/files/', blank=True, null=True, help_text="Fichier du certificat (PDF, etc.)")
    image = models.ImageField(upload_to='certificates/', blank=True, null=True, help_text="Image/thumbnail du certificat (optionnel)")
    credential_url = models.URLField(blank=True, help_text="Lien vers le certificat (optionnel)")
    verified = models.BooleanField(default=False, help_text="Indique si le certificat est vérifié")
    order = models.IntegerField(default=0, help_text="Ordre d'affichage")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order', '-issued_date']
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return f"{self.title} - {self.issuer}"


class Statistics(models.Model):
    """Statistiques affichées sur la page d'accueil"""
    projects_count = models.IntegerField(default=15, help_text="Nombre de projets réalisés")
    years_experience = models.IntegerField(default=3, help_text="Années d'expérience")
    technologies_count = models.IntegerField(default=25, help_text="Nombre de technologies maîtrisées")
    satisfaction_rate = models.IntegerField(default=100, help_text="Taux de satisfaction en %")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Statistiques'
        verbose_name_plural = 'Statistiques'

    def __str__(self):
        return f"Statistiques (Mis à jour: {self.updated_at.strftime('%d/%m/%Y')})"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_stats(cls):
        """Récupère ou crée l'instance unique de statistiques"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(models.Model):
    """Paramètres généraux du site"""
    tawk_to_widget_id = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="ID du widget Tawk.to (ex: 5f8a9b1c2d3e4f5g6h7i8j9k/default)"
    )
    enable_chat = models.BooleanField(
        default=True, 
        help_text="Activer/Désactiver le chat en direct"
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Paramètres du Site'
        verbose_name_plural = 'Paramètres du Site'

    def __str__(self):
        return f"Paramètres du Site (Mis à jour: {self.updated_at.strftime('%d/%m/%Y')})"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        """Récupère ou crée l'instance unique des paramètres"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj