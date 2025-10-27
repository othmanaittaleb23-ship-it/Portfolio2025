# Guide de Personnalisation du Portfolio

## 🎯 Actions Prioritaires

### 1. Mettre à Jour Votre Photo de Profil

**Méthode Rapide (URL):**
1. Ouvrez http://127.0.0.1:8000/admin/
2. Connectez-vous avec votre superutilisateur
3. Cliquez sur "About" → Cliquez sur votre nom
4. Dans le champ "Profile image", collez l'URL de votre photo
   - Exemple GitHub: `https://avatars.githubusercontent.com/u/VOTRE_ID`
   - Ou utilisez une image sur Imgur, Unsplash, etc.
5. Cliquez sur "Save"

**Pour trouver votre photo GitHub:**
- Allez sur https://github.com/3tttman
- Faites un clic droit sur votre avatar → "Copier l'adresse de l'image"

### 2. Mettre à Jour Vos Informations de Contact

Dans l'admin (http://127.0.0.1:8000/admin/portfolio/about/):
- **Email:** Remplacez `othman.ait.taleb@example.com` par votre vrai email
- **Téléphone:** Remplacez `+212 6XX XX XX XX` par votre numéro
- **LinkedIn:** Mettez votre vrai profil LinkedIn
- **Location:** Ajustez si nécessaire (actuellement "Maroc")

### 3. Ajouter Vos Vrais Projets

**Supprimer les projets d'exemple:**
1. Admin → Projects
2. Sélectionnez les projets d'exemple
3. Action → "Delete selected projects"

**Ajouter vos projets:**
1. Cliquez sur "Add Project"
2. Remplissez:
   - **Title:** Nom de votre projet
   - **Description:** Description détaillée
   - **Short description:** Résumé court (optionnel)
   - **Image:** URL d'une capture d'écran
   - **Technologies:** Ex: "Django, React, PostgreSQL" (séparés par des virgules)
   - **GitHub URL:** Lien vers votre repo GitHub
   - **Live URL:** Lien de démo (si disponible)
   - **Is featured:** Cochez pour mettre en avant
   - **Is active:** Cochez pour afficher

### 4. Ajuster Vos Compétences

Dans l'admin → Skills:
- Modifiez les niveaux (0-100) selon votre expertise réelle
- Ajoutez de nouvelles compétences si nécessaire
- Supprimez celles que vous ne maîtrisez pas

**Icônes disponibles (Font Awesome):**
- Python: `fab fa-python`
- JavaScript: `fab fa-js-square`
- React: `fab fa-react`
- Node.js: `fab fa-node`
- Docker: `fab fa-docker`
- Git: `fab fa-git-alt`
- Database: `fas fa-database`
- Plus d'icônes: https://fontawesome.com/icons

### 5. Mettre à Jour Votre Expérience

Dans l'admin → Experiences:
1. Modifiez ou supprimez les expériences d'exemple
2. Ajoutez vos vraies expériences professionnelles
3. Pour une expérience actuelle, cochez "Is current" et laissez "End date" vide

### 6. Mettre à Jour Votre Formation

Dans l'admin → Education:
1. Remplacez par vos vraies formations
2. Ajoutez diplômes, certifications, formations en ligne

## 🎨 Personnalisation Avancée

### Changer les Couleurs

Éditez `static/css/style.css` et modifiez les variables CSS:
```css
:root {
    --primary-color: #007bff;      /* Couleur principale */
    --secondary-color: #6c757d;    /* Couleur secondaire */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Modifier le Texte de Bienvenue

Éditez directement dans l'admin → About:
- **Name:** Votre nom
- **Title:** Votre titre professionnel
- **Description:** Votre présentation

### Ajouter des Réseaux Sociaux

Dans l'admin → About, remplissez:
- **LinkedIn:** URL complète de votre profil
- **GitHub:** URL de votre profil GitHub
- **Website:** Votre site web personnel (optionnel)

## 📸 Trouver des Images pour Vos Projets

**Sources d'images gratuites:**
- Unsplash: https://unsplash.com/
- Pexels: https://www.pexels.com/
- Vos propres captures d'écran (uploadez sur Imgur)

**Faire une capture d'écran de votre projet:**
1. Ouvrez votre projet dans le navigateur
2. Prenez une capture d'écran
3. Uploadez sur https://imgur.com/
4. Copiez le lien direct de l'image
5. Collez dans le champ "Image" de votre projet

## 🔄 Commandes Utiles

**Recharger les données d'exemple:**
```bash
python reload_data.py
```

**Créer un nouveau superutilisateur:**
```bash
python manage.py createsuperuser
```

**Démarrer le serveur:**
```bash
python manage.py runserver
```

**Sauvegarder vos données actuelles:**
```bash
python manage.py dumpdata portfolio > mes_donnees.json
```

**Restaurer des données sauvegardées:**
```bash
python manage.py loaddata mes_donnees.json
```

## 📝 Conseils pour un Portfolio Professionnel

### Pour les Projets:
- ✅ Utilisez des descriptions claires et concises
- ✅ Mentionnez les problèmes résolus
- ✅ Listez les technologies utilisées
- ✅ Ajoutez des liens GitHub et démos
- ✅ Utilisez des captures d'écran de qualité

### Pour les Compétences:
- ✅ Soyez honnête sur vos niveaux
- ✅ Mettez en avant vos points forts
- ✅ Groupez par catégories (Programming, Framework, Database, Tools)

### Pour l'Expérience:
- ✅ Utilisez des verbes d'action (Développé, Créé, Optimisé)
- ✅ Quantifiez quand possible (Ex: "Amélioration de 30%")
- ✅ Mentionnez les technologies utilisées

## 🚀 Déploiement (Optionnel)

Pour mettre votre portfolio en ligne, consultez:
- **Heroku:** https://www.heroku.com/ (gratuit)
- **PythonAnywhere:** https://www.pythonanywhere.com/ (gratuit)
- **Render:** https://render.com/ (gratuit)
- **Railway:** https://railway.app/ (gratuit)

## 🆘 Besoin d'Aide?

Si vous rencontrez des problèmes:
1. Vérifiez les erreurs dans le terminal
2. Consultez la documentation Django: https://docs.djangoproject.com/
3. Vérifiez que toutes les dépendances sont installées: `pip install -r requirements.txt`

## 📋 Checklist de Personnalisation

- [ ] Photo de profil mise à jour
- [ ] Email et téléphone corrects
- [ ] LinkedIn et GitHub à jour
- [ ] Projets réels ajoutés
- [ ] Compétences ajustées
- [ ] Expériences professionnelles complétées
- [ ] Formation/Éducation mise à jour
- [ ] Couleurs personnalisées (optionnel)
- [ ] Testé sur mobile et desktop
- [ ] Formulaire de contact configuré (optionnel)

Bon courage avec votre portfolio ! 🎉
