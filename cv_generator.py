import json
import csv
import random
from faker import Faker
from tqdm import tqdm
import pandas as pd

# Initialize Faker with French locale
fake = Faker(['fr_FR'])

# Specialties for IT/Tech CVs
SPECIALTIES = [
    "Développement Web", "Développement Mobile", "Intelligence Artificielle", 
    "Science des Données", "Sécurité Informatique", "DevOps", 
    "Administration Système", "Réseaux", "Cloud Computing",
    "Développement Frontend", "Développement Backend", "Développement Full Stack",
    "UX/UI Design", "Génie Logiciel", "Test et Qualité Logicielle",
    "Big Data", "Base de Données", "Architecture Informatique",
    "Gestion de Projet IT", "Support Technique"
]

# Common tech skills
TECH_SKILLS = [
    "JavaScript", "Python", "Java", "C#", "PHP", "Ruby", "Swift", "Kotlin", 
    "TypeScript", "Go", "Rust", "C++", "C", "Scala", "HTML", "CSS", 
    "React", "Angular", "Vue.js", "Node.js", "Express.js", "Django", "Flask",
    "Spring Boot", "Laravel", "ASP.NET", "Ruby on Rails", "Symfony",
    "PostgreSQL", "MySQL", "MongoDB", "SQLite", "Redis", "Oracle", "SQL Server",
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Jenkins", "Git",
    "Linux", "Windows Server", "TensorFlow", "PyTorch", "Scikit-learn", "Pandas",
    "Spark", "Hadoop", "Power BI", "Tableau", "JIRA", "Selenium", "JUnit", 
    "Jest", "Mocha", "Cypress", "GraphQL", "REST API", "WebSockets", "OAuth", 
    "JWT", "Agile", "Scrum", "Kanban", "CI/CD", "Microservices", "Serverless"
]

# Common educational institutions in France
INSTITUTIONS = [
    "Université de Paris", "Université Lyon 1", "Université de Bordeaux",
    "Université de Strasbourg", "Université de Lille", "Sorbonne Université",
    "École Polytechnique", "CentraleSupélec", "INSA Lyon", "ENSIMAG Grenoble",
    "EPITA", "Télécom Paris", "Télécom SudParis", "ENSEIRB-MATMECA",
    "Université Toulouse III - Paul Sabatier", "Université Nice Sophia Antipolis",
    "Université de Nantes", "École 42", "Epitech", "Supinfo",
    "ESGI", "ETNA", "IUT de Paris", "IUT de Lyon", "CESI"
]

# Common languages
LANGUAGES = ["Français", "Anglais", "Espagnol", "Allemand", "Italien", "Arabe", "Chinois", "Portugais", "Russe", "Japonais"]

# French cities
CITIES = [
    "Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Nantes", "Strasbourg", 
    "Montpellier", "Bordeaux", "Lille", "Rennes", "Reims", "Toulon", "Grenoble", 
    "Dijon", "Angers", "Le Mans", "Aix-en-Provence", "Brest", "Limoges", "Tours"
]

# Generate a random CV
def generate_cv():
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    specialty = random.choice(SPECIALTIES)
    
    # Choose between 3-10 random skills without duplicates
    num_skills = random.randint(3, 10)
    skills = random.sample(TECH_SKILLS, num_skills)
    
    # Generate random experience (1-15 years)
    experience_years = random.randint(1, 15)
    
    # Generate random number of projects (experience_years * random factor)
    projects_count = max(1, int(experience_years * random.uniform(0.8, 3.5)))
    
    # Generate 1-3 educational qualifications
    num_educations = random.randint(1, 3)
    education = []
    for _ in range(num_educations):
        degree_year = fake.random_int(2000, 2024)
        degree_level = random.choice(["Licence", "Master", "Doctorat", "DUT", "BTS", "Ingénieur"])
        degree_field = random.choice(["Informatique", "Génie Logiciel", "Systèmes d'Information", 
                                      "Intelligence Artificielle", "Réseaux et Télécommunications",
                                      "Science des Données", "Cybersécurité"])
        
        education.append({
            "diplome": f"{degree_level} {degree_field}",
            "etablissement": random.choice(INSTITUTIONS),
            "annee_obtention": degree_year
        })
    
    # Sort education by year (descending)
    education.sort(key=lambda x: x["annee_obtention"], reverse=True)
    
    # Choose 1-3 languages
    num_languages = random.randint(1, 3)
    languages = random.sample(LANGUAGES, num_languages)
    if "Français" not in languages:
        languages.append("Français")  # Always include French
    
    # Generate location
    city = random.choice(CITIES)
    
    # Create the CV
    cv = {
        "nom": f"{first_name} {last_name}",
        "email": f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}",
        "telephone": fake.phone_number(),
        "langue_cv": "fr",
        "specialité": specialty,
        "competences": skills,
        "annees_experience": experience_years,
        "projets_realises": projects_count,
        "formation": education,
        "langues": languages,
        "localisation": f"{city}, France"
    }
    
    return cv

# Generate 2000 CVs
def generate_cvs(count=2000):
    print(f"Generating {count} CV profiles...")
    cvs = []
    for _ in tqdm(range(count)):
        cvs.append(generate_cv())
    return cvs

# Flatten the nested structure for CSV
def flatten_cv(cv):
    flat_cv = cv.copy()
    
    # Convert competences array to string
    flat_cv['competences'] = ', '.join(cv['competences'])
    
    # Convert langues array to string
    flat_cv['langues'] = ', '.join(cv['langues'])
    
    # Handle formation (education) - take only the most recent one for simplicity in CSV
    if cv['formation']:
        most_recent = cv['formation'][0]
        flat_cv['diplome'] = most_recent['diplome']
        flat_cv['etablissement'] = most_recent['etablissement']
        flat_cv['annee_obtention'] = most_recent['annee_obtention']
    else:
        flat_cv['diplome'] = ""
        flat_cv['etablissement'] = ""
        flat_cv['annee_obtention'] = ""
    
    # Remove the original formation array
    del flat_cv['formation']
    
    return flat_cv

# Save CVs to CSV file
def save_to_csv(cvs, filename='cvs_data.csv'):
    if not cvs:
        print("No CVs to save.")
        return
    
    # Flatten the CV structures for CSV format
    flat_cvs = [flatten_cv(cv) for cv in cvs]
    
    # Get all possible keys to ensure all columns are included
    all_keys = set()
    for cv in flat_cvs:
        all_keys.update(cv.keys())
    
    # Write to CSV
    print(f"Saving {len(cvs)} CV profiles to {filename}...")
    df = pd.DataFrame(flat_cvs)
    df.to_csv(filename, index=False, encoding='utf-8-sig')  # utf-8-sig for Excel compatibility
    print(f"CVs successfully saved to {filename}")

# Save CVs to JSON file (for backup or further processing)
def save_to_json(cvs, filename='cvs_data.json'):
    print(f"Saving {len(cvs)} CV profiles to {filename}...")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cvs, f, ensure_ascii=False, indent=2)
    print(f"CVs successfully saved to {filename}")

if __name__ == "__main__":
    # Generate 2000 CVs
    cvs = generate_cvs(2000)
    
    # Save to CSV
    save_to_csv(cvs)
    
    # Optionally save to JSON for full data structure
    save_to_json(cvs)
    
    print("Process completed successfully!")
