import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Statistics, Project, Skill

# Compter les projets et compétences actuels
projects_count = Project.objects.filter(is_active=True).count()
skills_count = Skill.objects.filter(is_active=True).count()

# Créer ou mettre à jour les statistiques
stats = Statistics.get_stats()
stats.projects_count = projects_count if projects_count > 0 else 15
stats.years_experience = 3  # Modifiez selon votre expérience
stats.technologies_count = skills_count if skills_count > 0 else 25
stats.satisfaction_rate = 100
stats.save()

print(f"Statistiques initialisees:")
print(f"   - Projets: {stats.projects_count}")
print(f"   - Annees d'experience: {stats.years_experience}")
print(f"   - Technologies: {stats.technologies_count}")
print(f"   - Satisfaction: {stats.satisfaction_rate}%")
print(f"\nVous pouvez maintenant modifier ces valeurs dans l'admin Django!")
