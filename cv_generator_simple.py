import csv
import random
import string
from datetime import datetime, timedelta
import os

# Data sets for generating random values
first_names = ["Jean", "Marie", "Pierre", "Sophie", "Luc", "Isabelle", "Thomas", "Claire", "Nicolas", "Julie", 
               "Mathieu", "Camille", "Antoine", "Céline", "François", "Laura", "Michel", "Sarah", "Philippe", "Emma",
               "David", "Audrey", "Alexandre", "Nathalie", "Julien", "Caroline", "Olivier", "Aurélie", "Patrick", "Sandrine"]

last_names = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau",
              "Simon", "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier",
              "Morel", "Girard", "Andre", "Lefevre", "Mercier", "Dupont", "Lambert", "Bonnet", "Francois", "Martinez"]

email_domains = ["gmail.com", "yahoo.fr", "hotmail.fr", "outlook.com", "orange.fr", "free.fr", "sfr.fr", "laposte.net"]

specialties = [
    "Développement Web", "Développement Mobile", "Intelligence Artificielle", 
    "Science des Données", "Sécurité Informatique", "DevOps", 
    "Administration Système", "Réseaux", "Cloud Computing",
    "Développement Frontend", "Développement Backend", "Développement Full Stack",
    "UX/UI Design", "Génie Logiciel", "Test et Qualité Logicielle",
    "Big Data", "Base de Données", "Architecture Informatique",
    "Gestion de Projet IT", "Support Technique"
]

tech_skills = [
    "JavaScript", "Python", "Java", "C#", "PHP", "Ruby", "Swift", "Kotlin", 
    "TypeScript", "Go", "Rust", "C++", "C", "Scala", "HTML", "CSS", 
    "React", "Angular", "Vue.js", "Node.js", "Express.js", "Django", "Flask",
    "Spring Boot", "Laravel", "ASP.NET", "Ruby on Rails", "Symfony",
    "PostgreSQL", "MySQL", "MongoDB", "SQLite", "Redis", "Oracle", "SQL Server",
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Jenkins", "Git",
    "Linux", "Windows Server", "TensorFlow", "PyTorch", "Scikit-learn", "Pandas",
    "Spark", "Hadoop", "Power BI", "Tableau", "JIRA", "Selenium", "JUnit", 
    "Jest", "Mocha", "Cypress", "GraphQL", "REST API", "WebSockets", "OAuth"
]

institutions = [
    "Université de Paris", "Université Lyon 1", "Université de Bordeaux",
    "Université de Strasbourg", "Université de Lille", "Sorbonne Université",
    "École Polytechnique", "CentraleSupélec", "INSA Lyon", "ENSIMAG Grenoble",
    "EPITA", "Télécom Paris", "Télécom SudParis", "ENSEIRB-MATMECA",
    "Université Toulouse III - Paul Sabatier", "Université Nice Sophia Antipolis",
    "Université de Nantes", "École 42", "Epitech", "Supinfo"
]

degree_types = ["Licence", "Master", "Doctorat", "DUT", "BTS", "Ingénieur"]
degree_fields = ["Informatique", "Génie Logiciel", "Systèmes d'Information", 
                "Intelligence Artificielle", "Réseaux et Télécommunications",
                "Science des Données", "Cybersécurité"]

languages = ["Français", "Anglais", "Espagnol", "Allemand", "Italien", "Arabe", "Chinois", "Portugais", "Russe", "Japonais"]

cities = [
    "Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Nantes", "Strasbourg", 
    "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Toulon", "Grenoble", 
    "Dijon", "Angers", "Le Mans", "Aix-en-Provence", "Brest", "Limoges", "Tours"
]

def generate_phone_number():
    return f"+33 {random.randint(6, 7)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}"

def generate_random_cv():
    # Basic info
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    
    # Email
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}"
    
    # Phone number
    phone = generate_phone_number()
    
    # Specialty
    specialty = random.choice(specialties)
    
    # Skills (3-10 random skills)
    num_skills = random.randint(3, 10)
    skills = random.sample(tech_skills, num_skills)
    skills_str = ", ".join(skills)
    
    # Experience
    years_experience = random.randint(1, 15)
    
    # Projects
    projects_count = max(1, int(years_experience * random.uniform(0.8, 3.5)))
    
    # Most recent education
    degree_type = random.choice(degree_types)
    degree_field = random.choice(degree_fields)
    degree = f"{degree_type} {degree_field}"
    institution = random.choice(institutions)
    grad_year = random.randint(2000, 2024)
    
    # Languages (1-3 languages)
    num_langs = random.randint(1, 3)
    langs = random.sample(languages, num_langs)
    if "Français" not in langs:
        langs.append("Français")  # Always include French
    langs_str = ", ".join(langs)
    
    # Location
    city = random.choice(cities)
    location = f"{city}, France"
    
    return {
        "nom": full_name,
        "email": email,
        "telephone": phone,
        "langue_cv": "fr",
        "specialité": specialty,
        "competences": skills_str,
        "annees_experience": years_experience,
        "projets_realises": projects_count,
        "diplome": degree,
        "etablissement": institution,
        "annee_obtention": grad_year,
        "langues": langs_str,
        "localisation": location
    }

def generate_cvs(count=2000):
    print(f"Generating {count} CV profiles...")
    cvs = []
    for i in range(count):
        if i % 100 == 0 and i > 0:
            print(f"Generated {i} CVs...")
        cvs.append(generate_random_cv())
    return cvs

def save_to_csv(cvs, filename='cvs_data.csv'):
    print(f"Saving {len(cvs)} CV profiles to {filename}...")
    
    if not cvs:
        print("No CVs to save.")
        return
    
    # Get fieldnames from the first CV
    fieldnames = list(cvs[0].keys())
    
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cvs)
    
    print(f"CVs successfully saved to {filename}")
    print(f"CSV file size: {os.path.getsize(filename) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    print("Starting CV generator...")
    start_time = datetime.now()
    
    # Generate 2000 CVs
    cvs = generate_cvs(2000)
    
    # Save to CSV
    save_to_csv(cvs)
    
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Process completed successfully in {duration.total_seconds():.2f} seconds!")
