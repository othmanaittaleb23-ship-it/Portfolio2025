import json
import os
from datetime import datetime

def update_about():
    about = {
        "model": "portfolio.about",
        "pk": 1,
        "fields": {
            "name": "Othman Ait Taleb",
            "title": "Développeur Full Stack & Analyste de Données",
            "description": "Développeur passionné avec une expertise en développement web full-stack et analyse de données. Spécialisé dans la création de solutions web modernes et performantes avec Django, React et les technologies cloud. Expérience en développement d'applications web, analyse de données et optimisation de processus.",
            "profile_image": "/static/images/profile.jpg",
            "email": "othman.ait.taleb@example.com",
            "phone": "+212 6XX XX XX XX",
            "location": "Maroc",
            "linkedin": "https://linkedin.com/in/othman-ait-taleb",
            "github": "https://github.com/3tttman",
            "website": "",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    }
    return about

def update_skills():
    skills = [
        {
            "model": "portfolio.skill",
            "pk": 1,
            "fields": {
                "name": "Python",
                "level": 90,
                "icon": "fab fa-python",
                "category": "programming",
                "is_active": True,
                "order": 1
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 2,
            "fields": {
                "name": "Django",
                "level": 85,
                "icon": "fas fa-server",
                "category": "framework",
                "is_active": True,
                "order": 2
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 3,
            "fields": {
                "name": "JavaScript",
                "level": 80,
                "icon": "fab fa-js",
                "category": "programming",
                "is_active": True,
                "order": 3
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 4,
            "fields": {
                "name": "React",
                "level": 75,
                "icon": "fab fa-react",
                "category": "framework",
                "is_active": True,
                "order": 4
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 5,
            "fields": {
                "name": "SQL",
                "level": 85,
                "icon": "fas fa-database",
                "category": "database",
                "is_active": True,
                "order": 5
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 6,
            "fields": {
                "name": "Git",
                "level": 90,
                "icon": "fab fa-git-alt",
                "category": "tools",
                "is_active": True,
                "order": 6
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 7,
            "fields": {
                "name": "Docker",
                "level": 75,
                "icon": "fab fa-docker",
                "category": "tools",
                "is_active": True,
                "order": 7
            }
        },
        {
            "model": "portfolio.skill",
            "pk": 8,
            "fields": {
                "name": "Pandas",
                "level": 80,
                "icon": "fas fa-chart-line",
                "category": "programming",
                "is_active": True,
                "order": 8
            }
        }
    ]
    return skills

def update_experiences():
    experiences = [
        {
            "model": "portfolio.experience",
            "pk": 1,
            "fields": {
                "company": "Entreprise X",
                "position": "Développeur Full Stack",
                "start_date": "2022-01-01",
                "end_date": None,
                "is_current": True,
                "description": "Développement et maintenance d'applications web avec Django et React. Optimisation des performances et mise en place de bonnes pratiques de développement.",
                "company_logo": "",
                "order": 1
            }
        },
        {
            "model": "portfolio.experience",
            "pk": 2,
            "fields": {
                "company": "Entreprise Y",
                "position": "Analyste de Données",
                "start_date": "2020-01-01",
                "end_date": "2021-12-31",
                "is_current": False,
                "description": "Analyse de données et création de tableaux de bord pour la prise de décision. Utilisation de Python, Pandas et des outils de visualisation de données.",
                "company_logo": "",
                "order": 2
            }
        }
    ]
    return experiences

def update_education():
    education = [
        {
            "model": "portfolio.education",
            "pk": 1,
            "fields": {
                "degree": "Master en Informatique",
                "institution": "Université X",
                "field_of_study": "Informatique",
                "start_date": "2018-09-01",
                "end_date": "2020-06-30",
                "is_current": False,
                "description": "Spécialisation en développement web et analyse de données. Mémoire sur l'optimisation des performances des applications web.",
                "institution_logo": "",
                "order": 1
            }
        },
        {
            "model": "portfolio.education",
            "pk": 2,
            "fields": {
                "degree": "Licence en Informatique",
                "institution": "Université Y",
                "field_of_study": "Informatique",
                "start_date": "2015-09-01",
                "end_date": "2018-06-30",
                "is_current": False,
                "description": "Formation générale en informatique avec des cours en programmation, bases de données et réseaux.",
                "institution_logo": "",
                "order": 2
            }
        }
    ]
    return education

def update_projects():
    projects = [
        {
            "model": "portfolio.project",
            "pk": 1,
            "fields": {
                "title": "Portfolio Personnel",
                "description": "Développement d'un portfolio personnel avec Django et React pour présenter mes compétences et projets.",
                "short_description": "Portfolio personnel développé avec Django et React",
                "image": "/static/images/portfolio.jpg",
                "technologies": "Django, React, Bootstrap, PostgreSQL",
                "github_url": "https://github.com/3tttman/portfolio",
                "live_url": "https://othman-ait-taleb.vercel.app/",
                "is_featured": True,
                "is_active": True
            }
        },
        {
            "model": "portfolio.project",
            "pk": 2,
            "fields": {
                "title": "Application de Gestion de Tâches",
                "description": "Application web de gestion de tâches avec authentification utilisateur et interface réactive.",
                "short_description": "Gestion de tâches avec Django et JavaScript",
                "image": "/static/images/todo.jpg",
                "technologies": "Django, JavaScript, SQLite, Bootstrap",
                "github_url": "https://github.com/3tttman/todo-app",
                "live_url": "",
                "is_featured": True,
                "is_active": True
            }
        },
        {
            "model": "portfolio.project",
            "pk": 3,
            "fields": {
                "title": "Analyse de Données",
                "description": "Analyse de données avec Python et création de visualisations interactives.",
                "short_description": "Analyse de données avec Python et Pandas",
                "image": "/static/images/data-analysis.jpg",
                "technologies": "Python, Pandas, Matplotlib, Jupyter",
                "github_url": "https://github.com/3tttman/data-analysis",
                "live_url": "",
                "is_featured": True,
                "is_active": True
            }
        }
    ]
    return projects

def main():
    # Créer le dossier pour les images s'il n'existe pas
    os.makedirs("portfolio/static/images", exist_ok=True)
    
    # Mettre à jour les données
    data = []
    data.append(update_about())
    data.extend(update_skills())
    data.extend(update_experiences())
    data.extend(update_education())
    data.extend(update_projects())
    
    # Sauvegarder les données dans le fichier sample_data.json
    with open('portfolio/fixtures/sample_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Données mises à jour avec succès!")
    print("\nProchaines étapes :")
    print("1. Copiez votre photo de profil dans : portfolio/static/images/profile.jpg")
    print("2. Exécutez : python manage.py loaddata portfolio/fixtures/sample_data.json")
    print("3. Démarrez le serveur : python manage.py runserver")
    print("\nVotre portfolio sera accessible à l'adresse : http://127.0.0.1:8000/")

if __name__ == "__main__":
    main()
