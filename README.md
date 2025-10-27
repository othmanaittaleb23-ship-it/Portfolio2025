# 🚀 Portfolio - Othman Ait Taleb

Portfolio professionnel de **Othman Ait Taleb** - Développeur Full Stack spécialisé en Django, React et réseaux informatiques. Site moderne et responsive développé avec Django, Bootstrap et des animations CSS/JavaScript.

## 🚀 Fonctionnalités

- **Design moderne et responsive** avec Bootstrap 5
- **Animations fluides** et interactions utilisateur
- **Gestion de contenu** via l'interface d'administration Django
- **Sections complètes** : À propos, Projets, Compétences, Expérience, Formation, Contact
- **Formulaire de contact** fonctionnel avec envoi d'emails
- **Interface d'administration** personnalisée
- **Optimisé pour les performances** et le SEO

## 🛠️ Technologies Utilisées

- **Backend** : Django 4.2.7
- **Frontend** : HTML5, CSS3, JavaScript ES6+, Bootstrap 5
- **Base de données** : SQLite (développement)
- **Icônes** : Font Awesome 6
- **Polices** : Google Fonts (Inter)

## 📦 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone <votre-repo>
cd Portfolio2025
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Appliquer les migrations**
```bash
python manage.py migrate
```

4. **Charger les données d'exemple**
```bash
python manage.py loaddata portfolio/fixtures/sample_data.json
```

5. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

6. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

7. **Accéder au site**
- Site web : http://127.0.0.1:8000/
- Administration : http://127.0.0.1:8000/admin/

## 📁 Structure du Projet

```
Portfolio2025/
├── portfolio/                    # Application principale
│   ├── models.py               # Modèles de données
│   ├── views.py                # Vues
│   ├── urls.py                 # URLs
│   ├── admin.py                # Configuration admin
│   ├── forms.py                # Formulaires
│   └── templates/              # Templates HTML
│       └── portfolio/
│           ├── base.html       # Template de base
│           ├── home.html       # Page d'accueil
│           ├── about.html      # Page à propos
│           └── contact.html    # Page de contact
├── static/                     # Fichiers statiques
│   ├── css/
│   │   └── style.css          # CSS personnalisé
│   ├── js/
│   │   └── main.js            # JavaScript
│   └── images/                # Images
├── media/                    # Fichiers uploadés
├── portfolio_project/         # Configuration Django
└── requirements.txt          # Dépendances Python
```

## 🎨 Personnalisation

### Modifier le contenu
1. Accédez à l'interface d'administration : http://127.0.0.1:8000/admin/
2. Connectez-vous avec votre superutilisateur
3. Modifiez les sections :
   - **About** : Informations personnelles
   - **Projects** : Vos projets
   - **Skills** : Compétences techniques
   - **Experience** : Expérience professionnelle
   - **Education** : Formation
   - **Contact** : Messages reçus

### Personnaliser le design
- **CSS** : Modifiez `static/css/style.css`
- **JavaScript** : Modifiez `static/js/main.js`
- **Templates** : Modifiez les fichiers dans `portfolio/templates/portfolio/`

### Variables CSS personnalisables
```css
:root {
    --primary-color: #007bff;      /* Couleur principale */
    --secondary-color: #6c757d;    /* Couleur secondaire */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}
```

## 📱 Responsive Design

Le portfolio est entièrement responsive et s'adapte à tous les écrans :
- **Desktop** : Expérience complète avec animations
- **Tablet** : Interface optimisée pour les tablettes
- **Mobile** : Navigation simplifiée et contenu adapté

## 🚀 Déploiement

### Production
1. **Configurer les variables d'environnement**
```python
DEBUG = False
ALLOWED_HOSTS = ['votre-domaine.com']
```

2. **Configurer la base de données de production**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Collecter les fichiers statiques**
```bash
python manage.py collectstatic
```

4. **Déployer avec Gunicorn + Nginx** (recommandé)

## 📧 Configuration Email

Pour le formulaire de contact, configurez dans `settings.py` :
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'
DEFAULT_FROM_EMAIL = 'votre-email@gmail.com'
```

## 🤝 Contribution

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Othman Ait Taleb**
- Email : othman.ait.taleb@example.com
- LinkedIn : [linkedin.com/in/othman-ait-taleb](https://linkedin.com/in/othman-ait-taleb)
- GitHub : [github.com/othman-ait-taleb](https://github.com/othman-ait-taleb)

## 🙏 Remerciements

- Django pour le framework web
- Bootstrap pour le système de grille
- Font Awesome pour les icônes
- Unsplash pour les images d'exemple


