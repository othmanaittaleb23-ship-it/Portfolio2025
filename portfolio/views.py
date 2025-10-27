from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Project, Skill, Experience, Education, Contact, Certificate, Statistics, SiteSettings
from django.db import DatabaseError
import json


def group_skills(skills):
    """Retourne un dict groupant les skills selon les 6 catégories demandées."""
    categories = [
        'Réseaux',
        'Methodologiques',
        'Outils & plateformes',
        'Base Données',
        'Langages',
        'Systèmes'
    ]

    grouped = {c: [] for c in categories}

    for s in skills:
        name = (s.name or '').lower()

        # Réseaux
        if any(k in name for k in ['tcp', 'vlan', 'vpn', 'pare', 'pare-feu', 'parefeu']):
            grouped['Réseaux'].append(s)
            continue

        # Méthodologiques
        if any(k in name for k in ['uml', 'merise', 'agile', 'scrum']):
            grouped['Methodologiques'].append(s)
            continue

        # Systèmes
        if any(k in name for k in ['linux', 'windows', 'debian', 'ubuntu', 'centos', 'kali', 'server']):
            grouped['Systèmes'].append(s)
            continue

        # Base Données
        if s.category == 'database' or any(k in name for k in ['mysql', 'sql server', 'oracle', 'postgres']):
            grouped['Base Données'].append(s)
            continue

        # Langages
        if s.category == 'programming' or any(k in name for k in ['java', 'python', 'c++', 'c#', 'c /', 'bash', 'php', 'javascript', 'html', 'css']):
            grouped['Langages'].append(s)
            continue

        # Par défaut -> Outils & plateformes
        grouped['Outils & plateformes'].append(s)

    # Convertir en structure simple (list de dicts) pour la sérialisation JSON
    out = {}
    for k, lst in grouped.items():
        out[k] = [
            {
                'name': s.name,
                'level': s.level,
                'icon': s.icon or '',
            }
            for s in lst
        ]

    return out
from .forms import ContactForm

def home(request):
    """Vue principale du portfolio"""
    about = About.objects.first()
    projects = Project.objects.filter(is_active=True)[:6]
    skills = Skill.objects.filter(is_active=True)
    experiences = Experience.objects.all()[:5]
    education = Education.objects.all()[:3]
    stats = Statistics.get_stats()
    site_settings = SiteSettings.get_settings()
    
    grouped = group_skills(skills)

    context = {
        'about': about,
        'projects': projects,
        'skills': skills,
        'grouped_skills_json': json.dumps(grouped),
        'grouped_skills_keys': list(grouped.keys()),
        'experiences': experiences,
        'education': education,
        'stats': stats,
        'site_settings': site_settings,
    }
    return render(request, 'portfolio/home.html', context)

def project_detail(request, pk):
    """Détail d'un projet"""
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
    """Page de contact"""
    site_settings = SiteSettings.get_settings()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sauvegarder le message dans la base de données
            form.save()
            
            messages.success(request, 'Votre message a été envoyé avec succès! Je vous répondrai bientôt.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form, 'site_settings': site_settings})

def about_page(request):
    """Page À propos détaillée"""
    about = About.objects.first()
    skills = Skill.objects.filter(is_active=True)
    experiences = Experience.objects.all()
    education = Education.objects.all()
    site_settings = SiteSettings.get_settings()
    
    grouped = group_skills(skills)

    # Charger les certificats si la table existe, sinon fallback silencieux (utile avant migrations)
    certificates = []
    try:
        # Forcer l'évaluation de la QuerySet ici so it raises if the table is missing
        certificates = list(Certificate.objects.filter(is_active=True).order_by('-issued_date', '-order')[:12])
        # Chunk certificates into groups of 3 for the carousel slides
        cert_chunks = [certificates[i:i+3] for i in range(0, len(certificates), 3)]
    except DatabaseError:
        # La base de données n'est peut-être pas migrée dans l'environnement actuel.
        certificates = []
        cert_chunks = []

    context = {
        'about': about,
        'skills': skills,
        'grouped_skills_json': json.dumps(grouped),
        'grouped_skills_keys': list(grouped.keys()),
        'experiences': experiences,
        'education': education,
        'certificates': certificates,
        'cert_chunks': cert_chunks,
        'site_settings': site_settings,
    }
    return render(request, 'portfolio/about.html', context)