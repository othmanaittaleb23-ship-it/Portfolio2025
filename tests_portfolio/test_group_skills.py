from django.test import TestCase

from portfolio.models import Skill
from portfolio.views import group_skills


class GroupSkillsTests(TestCase):
    def test_group_skills_basic(self):
        # Create skills that should map to each category
        Skill.objects.create(name='TCP/IP', category='tools', level=70)
        Skill.objects.create(name='UML', category='tools', level=50)
        Skill.objects.create(name='Linux', category='tools', level=80)
        Skill.objects.create(name='MySQL', category='database', level=60)
        Skill.objects.create(name='Python', category='programming', level=90)
        Skill.objects.create(name='Docker', category='tools', level=65)

        skills = Skill.objects.filter(is_active=True)
        grouped = group_skills(skills)

        # Basic expectations: keys exist and contain expected names
        self.assertIn('Réseaux', grouped)
        self.assertIn('Methodologiques', grouped)
        self.assertIn('Systèmes', grouped)
        self.assertIn('Base Données', grouped)
        self.assertIn('Langages', grouped)
        self.assertIn('Outils & plateformes', grouped)

        # Check that specific skills landed in expected categories
        réseaux_names = [s['name'] for s in grouped['Réseaux']]
        self.assertIn('TCP/IP', réseaux_names)

        systèmes_names = [s['name'] for s in grouped['Systèmes']]
        self.assertIn('Linux', systèmes_names)

        bdd_names = [s['name'] for s in grouped['Base Données']]
        self.assertIn('MySQL', bdd_names)

        langages_names = [s['name'] for s in grouped['Langages']]
        self.assertIn('Python', langages_names)
