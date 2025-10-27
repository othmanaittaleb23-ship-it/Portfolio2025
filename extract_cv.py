import PyPDF2
import json
import os
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def update_sample_data(cv_text):
    """Met à jour le fixture en se basant sur le texte extrait du CV."""
    # Heuristiques simples pour extraire les champs clés
    def parse_cv_text(text: str) -> dict:
        # Normalisation de base
        normalized = re.sub(r"\u00A0", " ", text)

        patterns = {
            'email': r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            'phone': r"(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{2,3}\)?[\s.-]?)?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}",
            'linkedin': r"https?://(?:[\w.-]+\.)?linkedin\.com/[^\s]+",
            'github': r"https?://(?:www\.)?github\.com/[A-Za-z0-9_-]+",
        }

        extracted: dict[str, str] = {}

        for key, pat in patterns.items():
            m = re.search(pat, normalized, flags=re.IGNORECASE)
            if m:
                extracted[key] = m.group(0).strip()

        # Titre possible
        title_candidates = []
        for label in [
            r"(?i)(développeur|developer).{0,40}(full\s*stack|\bpython\b|django|data|analyst)",
            r"(?i)(ingénieur|engineer).{0,40}(logiciel|software)",
        ]:
            m = re.search(label, normalized)
            if m:
                title_candidates.append(m.group(0))
        if title_candidates:
            extracted['title'] = max(title_candidates, key=len).strip().replace("\n", " ")

        # Lieu (ville/pays) après un mot-clé
        loc = re.search(r"(?i)(Adresse|Address|Localisation|Location|Basé à|Based in)\s*[:\-]?\s*(.+)", normalized)
        if loc:
            extracted['location'] = loc.group(2).splitlines()[0].strip()

        # Nom: 1ère ligne avec deux mots capitalisés ou entête avant coordonnées
        lines = [l.strip() for l in normalized.splitlines() if l.strip()]
        if lines:
            # Cherche une ligne avec nom complet probable
            for line in lines[:6]:
                if re.match(r"^[A-ZÉÈÂÊÎÔÛÄËÏÖÜÀÇ][A-Za-zÉéÈèÊêÎîÔôÛûÄäËëÏïÖöÜüÀàÇç'\-]+\s+[A-ZÉÈÂÊÎÔÛÄËÏÖÜÀÇ][A-Za-zÉéÈèÊêÎîÔôÛûÄäËëÏïÖöÜüÀàÇç'\-]+(?:\s+[A-Z][A-Za-z'\-]+)?$", line):
                    extracted['name'] = line
                    break
            # Fallback: si on trouve "Othman" dans les 10 premières lignes
            if 'name' not in extracted:
                for line in lines[:10]:
                    if 'othman' in line.lower():
                        extracted['name'] = line
                        break

        return extracted

    def parse_experiences(text: str) -> list:
        """Extrait les expériences professionnelles du CV."""
        experiences = []
        normalized = re.sub(r"\u00A0", " ", text)
        
        # Patterns pour détecter les expériences
        exp_patterns = [
            r"(?i)(expérience|experience|travail|work|emploi|job|poste|position)",
            r"(?i)(stage|internship|alternance|apprentissage)",
            r"(?i)(freelance|freelancing|consultant|consulting)"
        ]
        
        # Chercher les sections d'expérience
        lines = [l.strip() for l in normalized.splitlines() if l.strip()]
        in_experience_section = False
        current_exp = {}
        
        for i, line in enumerate(lines):
            # Détecter le début d'une section expérience
            if any(re.search(pattern, line, re.IGNORECASE) for pattern in exp_patterns):
                in_experience_section = True
                continue
                
            if in_experience_section:
                # Détecter une nouvelle expérience (poste + entreprise)
                if re.match(r"^[A-Z][A-Za-z\s\-&]+$", line) and len(line) > 5:
                    if current_exp:
                        experiences.append(current_exp)
                    current_exp = {
                        'position': line,
                        'company': '',
                        'description': '',
                        'start_date': '',
                        'end_date': '',
                        'is_current': False
                    }
                # Détecter l'entreprise (souvent après le poste)
                elif current_exp and not current_exp['company'] and re.match(r"^[A-Z][A-Za-z\s\-&\.]+$", line):
                    current_exp['company'] = line
                # Détecter les dates
                elif re.search(r"\d{4}", line):
                    date_match = re.search(r"(\d{4})\s*[-–]\s*(\d{4}|présent|present|actuel|current)", line, re.IGNORECASE)
                    if date_match:
                        current_exp['start_date'] = date_match.group(1) + "-01-01"
                        if date_match.group(2).lower() in ['présent', 'present', 'actuel', 'current']:
                            current_exp['is_current'] = True
                        else:
                            current_exp['end_date'] = date_match.group(2) + "-12-31"
                # Description (lignes avec du texte descriptif)
                elif current_exp and len(line) > 20 and not re.match(r"^[A-Z][A-Za-z\s\-&]+$", line):
                    if current_exp['description']:
                        current_exp['description'] += " " + line
                    else:
                        current_exp['description'] = line
                        
        # Ajouter la dernière expérience
        if current_exp:
            experiences.append(current_exp)
            
        return experiences[:5]  # Limiter à 5 expériences

    def parse_education(text: str) -> list:
        """Extrait la formation du CV."""
        education = []
        normalized = re.sub(r"\u00A0", " ", text)
        
        # Patterns pour détecter la formation
        edu_patterns = [
            r"(?i)(formation|education|études|studies|diplôme|diploma|master|licence|bachelor|doctorat|phd)",
            r"(?i)(université|university|école|school|institut|institute|faculté|faculty)"
        ]
        
        lines = [l.strip() for l in normalized.splitlines() if l.strip()]
        in_education_section = False
        current_edu = {}
        
        for i, line in enumerate(lines):
            # Détecter le début d'une section formation
            if any(re.search(pattern, line, re.IGNORECASE) for pattern in edu_patterns):
                in_education_section = True
                continue
                
            if in_education_section:
                # Détecter un diplôme
                if re.search(r"(?i)(master|licence|bachelor|doctorat|phd|diplôme|diploma)", line):
                    if current_edu:
                        education.append(current_edu)
                    current_edu = {
                        'degree': line,
                        'institution': '',
                        'field_of_study': '',
                        'start_date': '',
                        'end_date': '',
                        'is_current': False,
                        'description': ''
                    }
                # Détecter l'institution
                elif current_edu and not current_edu.get('institution') and re.search(r"(?i)(université|university|école|school|institut|institute)", line):
                    current_edu['institution'] = line
                # Détecter les dates
                elif re.search(r"\d{4}", line):
                    date_match = re.search(r"(\d{4})\s*[-–]\s*(\d{4}|présent|present|actuel|current)", line, re.IGNORECASE)
                    if date_match:
                        current_edu['start_date'] = date_match.group(1) + "-09-01"
                        if date_match.group(2).lower() in ['présent', 'present', 'actuel', 'current']:
                            current_edu['is_current'] = True
                        else:
                            current_edu['end_date'] = date_match.group(2) + "-06-30"
                            
        # Ajouter la dernière formation
        if current_edu:
            education.append(current_edu)
            
        return education[:3]  # Limiter à 3 formations

    def parse_skills(text: str) -> list:
        """Extrait les compétences techniques du CV."""
        skills = []
        normalized = re.sub(r"\u00A0", " ", text)
        
        # Compétences techniques communes
        tech_skills = {
            'Python': {'level': 90, 'icon': 'fab fa-python', 'category': 'programming'},
            'Django': {'level': 85, 'icon': 'fas fa-server', 'category': 'framework'},
            'JavaScript': {'level': 80, 'icon': 'fab fa-js', 'category': 'programming'},
            'React': {'level': 75, 'icon': 'fab fa-react', 'category': 'framework'},
            'SQL': {'level': 85, 'icon': 'fas fa-database', 'category': 'database'},
            'Git': {'level': 90, 'icon': 'fab fa-git-alt', 'category': 'tools'},
            'Docker': {'level': 75, 'icon': 'fab fa-docker', 'category': 'tools'},
            'Pandas': {'level': 80, 'icon': 'fas fa-chart-line', 'category': 'programming'},
            'HTML': {'level': 85, 'icon': 'fab fa-html5', 'category': 'programming'},
            'CSS': {'level': 80, 'icon': 'fab fa-css3-alt', 'category': 'programming'},
            'Bootstrap': {'level': 75, 'icon': 'fab fa-bootstrap', 'category': 'framework'},
            'PostgreSQL': {'level': 80, 'icon': 'fas fa-database', 'category': 'database'},
            'MySQL': {'level': 75, 'icon': 'fas fa-database', 'category': 'database'},
            'Linux': {'level': 70, 'icon': 'fab fa-linux', 'category': 'tools'},
            'AWS': {'level': 65, 'icon': 'fab fa-aws', 'category': 'tools'},
            'Node.js': {'level': 70, 'icon': 'fab fa-node-js', 'category': 'framework'},
            'Vue.js': {'level': 65, 'icon': 'fab fa-vue', 'category': 'framework'},
            'Angular': {'level': 60, 'icon': 'fab fa-angular', 'category': 'framework'},
            'MongoDB': {'level': 70, 'icon': 'fas fa-database', 'category': 'database'},
            'Redis': {'level': 65, 'icon': 'fas fa-database', 'category': 'database'},
            'Nginx': {'level': 60, 'icon': 'fas fa-server', 'category': 'tools'},
            'Jenkins': {'level': 55, 'icon': 'fab fa-jenkins', 'category': 'tools'},
            'Kubernetes': {'level': 50, 'icon': 'fab fa-docker', 'category': 'tools'},
            'TensorFlow': {'level': 60, 'icon': 'fas fa-brain', 'category': 'programming'},
            'Scikit-learn': {'level': 70, 'icon': 'fas fa-chart-line', 'category': 'programming'},
            'Jupyter': {'level': 80, 'icon': 'fas fa-book', 'category': 'tools'},
            'Matplotlib': {'level': 75, 'icon': 'fas fa-chart-line', 'category': 'programming'},
            'Seaborn': {'level': 70, 'icon': 'fas fa-chart-line', 'category': 'programming'},
            'NumPy': {'level': 80, 'icon': 'fas fa-calculator', 'category': 'programming'},
            'Flask': {'level': 70, 'icon': 'fas fa-flask', 'category': 'framework'},
            'FastAPI': {'level': 75, 'icon': 'fas fa-bolt', 'category': 'framework'},
            'Celery': {'level': 65, 'icon': 'fas fa-tasks', 'category': 'tools'},
            'Elasticsearch': {'level': 60, 'icon': 'fas fa-search', 'category': 'database'},
            'GraphQL': {'level': 55, 'icon': 'fas fa-project-diagram', 'category': 'programming'},
            'REST API': {'level': 85, 'icon': 'fas fa-plug', 'category': 'programming'},
            'Microservices': {'level': 70, 'icon': 'fas fa-cubes', 'category': 'programming'},
            'CI/CD': {'level': 75, 'icon': 'fas fa-sync', 'category': 'tools'},
            'Agile': {'level': 80, 'icon': 'fas fa-users', 'category': 'soft'},
            'Scrum': {'level': 75, 'icon': 'fas fa-tasks', 'category': 'soft'},
            'Leadership': {'level': 70, 'icon': 'fas fa-crown', 'category': 'soft'},
            'Communication': {'level': 85, 'icon': 'fas fa-comments', 'category': 'soft'},
            'Problem Solving': {'level': 90, 'icon': 'fas fa-puzzle-piece', 'category': 'soft'},
            'Teamwork': {'level': 85, 'icon': 'fas fa-handshake', 'category': 'soft'}
        }
        
        # Chercher les compétences mentionnées dans le CV
        found_skills = []
        for skill_name, skill_data in tech_skills.items():
            if re.search(rf"\b{re.escape(skill_name)}\b", normalized, re.IGNORECASE):
                found_skills.append({
                    'name': skill_name,
                    'level': skill_data['level'],
                    'icon': skill_data['icon'],
                    'category': skill_data['category'],
                    'is_active': True,
                    'order': len(found_skills) + 1
                })
        
        return found_skills[:15]  # Limiter à 15 compétences

    extracted = parse_cv_text(cv_text)
    experiences = parse_experiences(cv_text)
    education = parse_education(cv_text)
    skills = parse_skills(cv_text)

    # Lire le fixture existant
    with open('portfolio/fixtures/sample_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Mettre à jour les informations personnelles si trouvées
    for item in data:
        if item.get('model') == 'portfolio.about':
            about = item['fields']
            if extracted.get('name'):
                about['name'] = extracted['name']
            if extracted.get('title'):
                about['title'] = extracted['title']
            if extracted.get('email'):
                about['email'] = extracted['email']
            if extracted.get('phone'):
                about['phone'] = extracted['phone']
            if extracted.get('location'):
                about['location'] = extracted['location']
            if extracted.get('linkedin'):
                about['linkedin'] = extracted['linkedin']
            if extracted.get('github'):
                about['github'] = extracted['github']
            # Conserver la photo et le CV existants; l'utilisateur peut les mettre à jour séparément
            break

    # Remplacer les expériences existantes par celles du CV
    data = [item for item in data if item.get('model') != 'portfolio.experience']
    for i, exp in enumerate(experiences):
        if exp.get('position') and exp.get('company'):
            data.append({
                "model": "portfolio.experience",
                "pk": i + 1,
                "fields": {
                    "company": exp['company'],
                    "position": exp['position'],
                    "description": exp.get('description', ''),
                    "start_date": exp.get('start_date', '2020-01-01'),
                    "end_date": exp.get('end_date'),
                    "is_current": exp.get('is_current', False),
                    "company_logo": "",
                    "order": i + 1
                }
            })

    # Remplacer les formations existantes par celles du CV
    data = [item for item in data if item.get('model') != 'portfolio.education']
    for i, edu in enumerate(education):
        if edu.get('degree'):
            data.append({
                "model": "portfolio.education",
                "pk": i + 1,
                "fields": {
                    "institution": edu.get('institution', 'Institution non spécifiée'),
                    "degree": edu['degree'],
                    "field_of_study": edu.get('field_of_study', ''),
                    "start_date": edu.get('start_date', '2018-09-01'),
                    "end_date": edu.get('end_date'),
                    "is_current": edu.get('is_current', False),
                    "description": edu.get('description', ''),
                    "institution_logo": "",
                    "order": i + 1
                }
            })

    # Remplacer les compétences existantes par celles du CV
    data = [item for item in data if item.get('model') != 'portfolio.skill']
    for i, skill in enumerate(skills):
        data.append({
            "model": "portfolio.skill",
            "pk": i + 1,
            "fields": {
                "name": skill['name'],
                "level": skill['level'],
                "icon": skill['icon'],
                "category": skill['category'],
                "is_active": skill['is_active'],
                "order": skill['order']
            }
        })

    # Sauvegarder les modifications
    with open('portfolio/fixtures/sample_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    cv_path = r'C:\Users\3tttman\CascadeProjects\Portfolio2025\CV_2025-10-16_Othman_Ait taleb.pdf'
    
    # Extraire le texte du CV
    try:
        cv_text = extract_text_from_pdf(cv_path)
        print("CV extrait avec succès!")
        print(f"Longueur du texte extrait: {len(cv_text)} caractères")
        
        # Mettre à jour les données
        update_sample_data(cv_text)
        print("Données mises à jour avec succès!")
        
        print("\nProchaines étapes:")
        print("1. Copiez votre photo de profil dans: portfolio/static/images/profile.jpg")
        print("2. Exécutez: python manage.py loaddata portfolio/fixtures/sample_data.json")
        print("3. Démarrez le serveur: python manage.py runserver")
        
    except Exception as e:
        print(f"Erreur: {str(e)}")
        import traceback
        traceback.print_exc()
        print("Assurez-vous que le fichier CV est au bon emplacement.")

if __name__ == "__main__":
    main()
