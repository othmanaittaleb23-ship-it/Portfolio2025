#!/usr/bin/env python
"""
Script pour recharger les données du portfolio
Ce script supprime les anciennes données et charge les nouvelles depuis le fichier fixtures
"""
import os
import sys
import django

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import About, Skill, Project, Experience, Education, Contact
from django.core.management import call_command

def reload_data():
    """Recharge les données du portfolio"""
    print(">> Suppression des anciennes donnees...")
    
    # Supprimer les anciennes données
    Contact.objects.all().delete()
    Education.objects.all().delete()
    Experience.objects.all().delete()
    Project.objects.all().delete()
    Skill.objects.all().delete()
    About.objects.all().delete()
    
    print(">> Anciennes donnees supprimees")
    
    print("\n>> Chargement des nouvelles donnees...")
    
    # Charger les nouvelles données
    call_command('loaddata', 'portfolio/fixtures/sample_data.json')
    
    print(">> Nouvelles donnees chargees avec succes!")
    
    # Afficher un résumé
    print("\n>> Resume des donnees:")
    print(f"   - About: {About.objects.count()}")
    print(f"   - Skills: {Skill.objects.count()}")
    print(f"   - Projects: {Project.objects.count()}")
    print(f"   - Experiences: {Experience.objects.count()}")
    print(f"   - Education: {Education.objects.count()}")
    print(f"   - Messages: {Contact.objects.count()}")
    
    print("\n>> Termine! Vous pouvez maintenant acceder a votre portfolio.")
    print("   URL: http://127.0.0.1:8000/")
    print("   Admin: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    reload_data()
