# 📚 Guide d'Utilisation de l'Administration

## 🎯 Accès à l'Administration

**URL:** `http://127.0.0.1:8000/admin/`

**Identifiants:** Utilisez les identifiants de superutilisateur que vous avez créés.

---

## 📝 Sections de l'Administration

### 1. **À Propos (About)** 👤

Gérez vos informations personnelles affichées sur le portfolio.

**Champs importants:**
- ✅ **Nom** : Votre nom complet
- ✅ **Titre** : Votre titre professionnel (ex: "Développeur Full Stack")
- ✅ **Description** : Votre présentation (affichée sur la page d'accueil)
- ✅ **Photo de profil** : Image affichée sur la page d'accueil
- ✅ **CV** : Fichier PDF de votre CV (téléchargeable via le bouton flottant)
- ✅ **Email, Téléphone, Localisation** : Vos coordonnées
- ✅ **LinkedIn, GitHub, Website** : Vos liens de réseaux sociaux

**Aperçus disponibles:**
- Photo de profil en miniature dans la liste
- Aperçu large de la photo dans le formulaire
- Statut du CV (Disponible/Manquant)

---

### 2. **Projets (Projects)** 💼

Gérez vos projets professionnels.

**Champs importants:**
- ✅ **Titre** : Nom du projet
- ✅ **Description courte** : Résumé (max 300 caractères)
- ✅ **Description** : Description détaillée
- ✅ **Image** : Screenshot ou logo du projet
- ✅ **Technologies** : Liste séparée par virgules (ex: "Django, React, PostgreSQL")
- ✅ **GitHub URL** : Lien vers le repository
- ✅ **GitHub URL 2** : Lien vers un second repository (backend par exemple)
- ✅ **Live URL** : Lien vers la démo en ligne
- ✅ **En vedette** : Cochez pour afficher en premier
- ✅ **Actif** : Cochez pour afficher sur le site

**Fonctionnalités:**
- 🎨 Aperçu de l'image en miniature
- ⭐ Badge "EN VEDETTE" pour les projets importants
- 🛠️ Compteur de technologies
- 🔗 Indicateur de liens disponibles
- 📅 Hiérarchie par date de création

**Filtres de projets:**
Les projets sont automatiquement filtrables par technologie sur le site:
- **Web** : HTML, CSS, JavaScript, React, Vue
- **Mobile** : Android, iOS, Flutter, React Native
- **Full Stack** : Django, Node, Express, Spring
- **Autres** : Tous les autres projets

---

### 3. **Compétences (Skills)** 🎯

Gérez vos compétences techniques.

**Champs importants:**
- ✅ **Nom** : Nom de la compétence (ex: "Python")
- ✅ **Catégorie** : Type de compétence
  - Programming (Bleu)
  - Framework (Violet)
  - Database (Orange)
  - Tool (Vert)
  - Other (Gris)
- ✅ **Icône** : Classe Font Awesome (ex: "fab fa-python")
- ✅ **Niveau** : 0-100 (pourcentage de maîtrise)
- ✅ **Ordre** : Ordre d'affichage (plus petit = affiché en premier)
- ✅ **Actif** : Cochez pour afficher sur le site

**Fonctionnalités:**
- 🎨 Aperçu de l'icône en couleur
- 🏷️ Badge de catégorie coloré
- 📊 Barre de progression visuelle du niveau
- ✓ Indicateur actif/inactif

**Icônes Font Awesome:**
Exemples d'icônes courantes:
- Python: `fab fa-python`
- JavaScript: `fab fa-js`
- React: `fab fa-react`
- Django: `fas fa-code`
- Docker: `fab fa-docker`
- Git: `fab fa-git-alt`

---

### 4. **Expériences (Experiences)** 💼

Gérez votre parcours professionnel.

**Champs importants:**
- ✅ **Entreprise** : Nom de l'entreprise
- ✅ **Poste** : Votre titre/fonction
- ✅ **Description** : Vos missions et réalisations
- ✅ **Logo de l'entreprise** : Logo affiché dans la timeline
- ✅ **Date de début** : Date de début du contrat
- ✅ **Date de fin** : Date de fin (laissez vide si en cours)
- ✅ **En cours** : Cochez si vous travaillez actuellement dans cette entreprise
- ✅ **Ordre** : Ordre d'affichage

**Fonctionnalités:**
- 🏢 Aperçu du logo de l'entreprise
- 📅 Affichage automatique de la période
- ✓ Badge "En cours" pour le poste actuel

---

### 5. **Formation (Education)** 🎓

Gérez votre parcours académique.

**Champs importants:**
- ✅ **Institution** : Nom de l'école/université
- ✅ **Diplôme** : Nom du diplôme obtenu
- ✅ **Domaine d'étude** : Spécialisation
- ✅ **Description** : Détails supplémentaires
- ✅ **Logo de l'institution** : Logo affiché
- ✅ **Date de début / fin**
- ✅ **En cours** : Cochez si vous êtes encore en formation
- ✅ **Ordre** : Ordre d'affichage

---

### 6. **Certificats (Certificates)** 🏆

Gérez vos certifications et badges.

**Champs importants:**
- ✅ **Titre** : Nom du certificat
- ✅ **Émetteur** : Organisation qui a délivré le certificat
- ✅ **Date d'émission** : Date d'obtention
- ✅ **Description** : Détails du certificat
- ✅ **Fichier** : PDF du certificat
- ✅ **Image** : Image du certificat (alternative au PDF)
- ✅ **URL de vérification** : Lien vers la page de vérification
- ✅ **Vérifié** : Cochez pour afficher le badge de vérification
- ✅ **Actif** : Cochez pour afficher sur le site
- ✅ **Ordre** : Ordre d'affichage

**Fonctionnalités:**
- 🖼️ Aperçu de l'image ou icône PDF
- ✓ Badge "Vérifié" avec icône
- 📅 Hiérarchie par date d'émission

---

### 7. **Messages de Contact (Contact)** 📧

Gérez les messages reçus via le formulaire de contact.

**Champs:**
- 📧 **Nom** : Nom de l'expéditeur
- 📧 **Email** : Email de l'expéditeur
- 📧 **Sujet** : Sujet du message
- 📧 **Message** : Contenu du message
- ✓ **Lu** : Marquez comme lu/non lu
- 📅 **Date de création** : Date de réception

**Fonctionnalités:**
- 📝 Aperçu du message (50 premiers caractères)
- 🏷️ Badge de statut (Lu/Non lu)
- 📅 Hiérarchie par date
- ⚡ Actions en masse :
  - "Marquer comme lu"
  - "Marquer comme non lu"

**Filtres:**
- Par statut (Lu/Non lu)
- Par date de création

---

## 🎨 Nouvelles Fonctionnalités de l'Admin

### **Aperçus Visuels**
- ✅ Toutes les images ont des aperçus miniatures dans les listes
- ✅ Aperçus en grande taille dans les formulaires d'édition
- ✅ Icônes Font Awesome affichées en couleur

### **Badges Colorés**
- ✅ Statuts visuels (Actif/Inactif, Lu/Non lu, Vérifié/Non vérifié)
- ✅ Catégories colorées pour les compétences
- ✅ Badges "EN VEDETTE" et "En cours"

### **Barres de Progression**
- ✅ Niveau de compétences affiché visuellement
- ✅ Couleurs adaptatives (vert ≥70%, orange ≥40%, gris <40%)

### **Actions Rapides**
- ✅ Édition en ligne pour certains champs
- ✅ Actions en masse pour les messages
- ✅ Filtres avancés sur toutes les sections

### **Design Moderne**
- ✅ Palette de couleurs vert/noir/gris/blanc
- ✅ Emojis dans les titres de sections
- ✅ Descriptions d'aide pour chaque section
- ✅ Interface responsive et professionnelle

---

## 💡 Conseils d'Utilisation

### **Pour les Projets:**
1. Ajoutez toujours une image de qualité
2. Listez les technologies séparées par des virgules
3. Marquez vos meilleurs projets comme "En vedette"
4. Ajoutez des liens GitHub et démo quand possible

### **Pour les Compétences:**
1. Utilisez des icônes Font Awesome appropriées
2. Soyez honnête sur les niveaux (70%+ = Expert, 40-70% = Intermédiaire, <40% = Débutant)
3. Organisez l'ordre pour mettre vos meilleures compétences en premier

### **Pour les Expériences:**
1. Ajoutez les logos d'entreprises pour un rendu professionnel
2. Décrivez vos réalisations avec des résultats chiffrés
3. Cochez "En cours" pour votre poste actuel

### **Pour les Certificats:**
1. Téléchargez soit un PDF soit une image
2. Cochez "Vérifié" pour les certificats officiels
3. Ajoutez l'URL de vérification quand disponible

---

## 🚀 Accès Rapide

- **Page d'accueil du site:** `http://127.0.0.1:8000/`
- **Administration:** `http://127.0.0.1:8000/admin/`
- **Page À propos:** `http://127.0.0.1:8000/about/`
- **Contact:** `http://127.0.0.1:8000/contact/`

---

## 📞 Support

Pour toute question ou problème, consultez la documentation Django ou contactez votre développeur.

**Bonne gestion de votre portfolio ! 🎉**
