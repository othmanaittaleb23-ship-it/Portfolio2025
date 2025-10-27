# 🚀 Guide de Déploiement sur PythonAnywhere

## 📋 Prérequis
- ✅ Compte GitHub (pour héberger le code)
- ✅ Compte PythonAnywhere gratuit
- ✅ Votre portfolio Django prêt

---

## 🎯 Étape 1 : Créer un Compte PythonAnywhere (5 min)

1. **Allez sur** : https://www.pythonanywhere.com/registration/register/beginner/
2. **Créez un compte gratuit** :
   - Username : `othman` (ou votre choix)
   - Email : votre email
   - Password : mot de passe sécurisé
3. **Confirmez votre email**
4. **Connectez-vous** : https://www.pythonanywhere.com/login/

---

## 📦 Étape 2 : Pousser le Code sur GitHub (10 min)

### **2.1 Créer un Repository GitHub**

1. **Allez sur** : https://github.com/new
2. **Nom du repository** : `Portfolio2025`
3. **Visibilité** : Public (ou Private)
4. **Cliquez sur** "Create repository"

### **2.2 Pousser le Code**

Ouvrez PowerShell dans votre dossier projet et exécutez :

```powershell
# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - Portfolio Django avec SEO"

# Ajouter le remote GitHub (REMPLACEZ par VOTRE URL)
git remote add origin https://github.com/VOTRE_USERNAME/Portfolio2025.git

# Pousser le code
git branch -M main
git push -u origin main
```

**⚠️ Important** : Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub !

---

## 🖥️ Étape 3 : Configuration sur PythonAnywhere (15 min)

### **3.1 Ouvrir une Console Bash**

1. **Connectez-vous** à PythonAnywhere
2. **Cliquez sur** "Consoles" dans le menu
3. **Cliquez sur** "Bash" pour ouvrir une nouvelle console

### **3.2 Cloner le Repository**

Dans la console Bash, tapez :

```bash
# Cloner votre repository (REMPLACEZ par VOTRE URL)
git clone https://github.com/VOTRE_USERNAME/Portfolio2025.git

# Aller dans le dossier
cd Portfolio2025
```

### **3.3 Créer un Environnement Virtuel**

```bash
# Créer l'environnement virtuel
mkvirtualenv --python=/usr/bin/python3.10 portfolio_env

# Activer l'environnement (automatique après création)
# Si besoin de réactiver plus tard : workon portfolio_env

# Installer les dépendances
pip install -r requirements.txt
```

### **3.4 Configuration de la Base de Données**

```bash
# Créer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser
# Username : admin (ou votre choix)
# Email : votre email
# Password : mot de passe sécurisé
```

### **3.5 Collecter les Fichiers Statiques**

```bash
python manage.py collectstatic --noinput
```

---

## 🌐 Étape 4 : Configurer l'Application Web (10 min)

### **4.1 Créer une Web App**

1. **Allez dans** "Web" dans le menu PythonAnywhere
2. **Cliquez sur** "Add a new web app"
3. **Choisissez** "Manual configuration"
4. **Sélectionnez** "Python 3.10"
5. **Cliquez sur** "Next"

### **4.2 Configuration du Virtual Environment**

Dans la section **"Virtualenv"** :
- **Cliquez sur** "Enter path to a virtualenv"
- **Entrez** : `/home/VOTRE_USERNAME/.virtualenvs/portfolio_env`
- **Remplacez** `VOTRE_USERNAME` par votre username PythonAnywhere

### **4.3 Configuration du WSGI File**

1. **Cliquez sur** le lien du fichier WSGI (ex: `/var/www/othman_pythonanywhere_com_wsgi.py`)
2. **Supprimez tout le contenu**
3. **Collez ce code** :

```python
import os
import sys

# Ajouter le chemin du projet
path = '/home/VOTRE_USERNAME/Portfolio2025'
if path not in sys.path:
    sys.path.append(path)

# Définir les settings Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

# Importer l'application WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**⚠️ Important** : Remplacez `VOTRE_USERNAME` par votre username PythonAnywhere !

4. **Cliquez sur** "Save"

### **4.4 Configuration des Fichiers Statiques**

Dans la section **"Static files"** :

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/VOTRE_USERNAME/Portfolio2025/staticfiles` |
| `/media/` | `/home/VOTRE_USERNAME/Portfolio2025/media` |

**Cliquez sur** le ✓ vert pour sauvegarder chaque ligne.

---

## ⚙️ Étape 5 : Configuration Django pour Production

### **5.1 Modifier settings.py**

Retournez dans la console Bash et éditez `settings.py` :

```bash
cd ~/Portfolio2025/portfolio_project
nano settings.py
```

**Modifiez ces lignes** :

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['othman.pythonanywhere.com', 'www.othman.pythonanywhere.com']

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**Sauvegardez** : `Ctrl+O`, `Enter`, `Ctrl+X`

---

## 🚀 Étape 6 : Lancer le Site !

1. **Retournez dans** l'onglet "Web" de PythonAnywhere
2. **Cliquez sur** le gros bouton vert **"Reload"**
3. **Attendez** 10 secondes
4. **Cliquez sur** le lien de votre site : `https://othman.pythonanywhere.com`

**🎉 Votre site est en ligne !**

---

## 📊 Étape 7 : Remplir le Contenu via l'Admin

1. **Allez sur** : `https://othman.pythonanywhere.com/admin/`
2. **Connectez-vous** avec le superuser créé
3. **Remplissez** :
   - ✅ About (informations personnelles)
   - ✅ Projects (vos projets)
   - ✅ Skills (compétences)
   - ✅ Experience (expériences)
   - ✅ Education (formations)
   - ✅ Certificates (certificats)

---

## 🔍 Étape 8 : Soumettre à Google (Après déploiement)

### **8.1 Google Search Console**

1. **Allez sur** : https://search.google.com/search-console
2. **Ajoutez votre site** : `https://othman.pythonanywhere.com`
3. **Vérifiez la propriété** (méthode HTML tag recommandée)
4. **Soumettez le sitemap** : `https://othman.pythonanywhere.com/sitemap.xml`
5. **Attendez 24-48h** pour l'indexation

### **8.2 Vérifier l'Indexation**

Tapez dans Google : `site:othman.pythonanywhere.com`

---

## 🔄 Mise à Jour du Site (Après modifications)

Quand vous modifiez le code localement :

```bash
# 1. Pousser sur GitHub
git add .
git commit -m "Description des modifications"
git push

# 2. Sur PythonAnywhere (Console Bash)
cd ~/Portfolio2025
git pull
python manage.py collectstatic --noinput
python manage.py migrate

# 3. Recharger l'application
# Allez dans Web > Reload
```

---

## 🎯 Checklist Finale

- [ ] Site accessible sur `https://othman.pythonanywhere.com`
- [ ] Admin accessible sur `https://othman.pythonanywhere.com/admin/`
- [ ] Contenu rempli (About, Projects, Skills, etc.)
- [ ] Images uploadées
- [ ] CV uploadé
- [ ] Sitemap accessible : `https://othman.pythonanywhere.com/sitemap.xml`
- [ ] Robots.txt accessible : `https://othman.pythonanywhere.com/robots.txt`
- [ ] Site soumis à Google Search Console
- [ ] Badge "Recherche Stage PFE" visible
- [ ] Formulaire de contact fonctionne

---

## 🆘 Dépannage

### **Erreur 500**
- Vérifiez les logs : Web > Log files > Error log
- Vérifiez que `DEBUG = False` et `ALLOWED_HOSTS` est correct

### **CSS ne charge pas**
- Vérifiez les chemins Static files dans Web
- Relancez `python manage.py collectstatic`
- Cliquez sur Reload

### **Images ne s'affichent pas**
- Vérifiez le chemin Media files dans Web
- Uploadez les images via l'admin

---

## 📞 Support

**PythonAnywhere Forums** : https://www.pythonanywhere.com/forums/
**Documentation** : https://help.pythonanywhere.com/

---

**Bon déploiement ! 🚀**
