# TuniHire CV Generator

![TuniHire CV Generator](https://img.shields.io/badge/TuniHire-CV%20Generator-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A powerful Python-based tool for generating large datasets of realistic CV/resume profiles for testing and development purposes.

## 🚀 Overview

The TuniHire CV Generator creates thousands of randomized yet realistic CV profiles designed to simulate real-world resume data. Perfect for testing HR applications, recruitment platforms, or data analysis tools that work with professional profiles.

## ✨ Features

- **Mass Profile Generation**: Create 2000+ CV profiles in seconds
- **Realistic French Data**: Specialized for French market with appropriate names, educational institutions, phone numbers, etc.
- **Tech Focus**: Particularly tailored for IT/Tech sector CVs
- **CSV Export**: Results saved in standard CSV format for easy integration with other systems
- **Customizable Fields**: All major CV components are included:
  - Personal information (name, email, phone)
  - Professional specialties and skills
  - Education history
  - Languages and experience levels
  - Projects and location data

## 📋 Generated Data Structure

Each generated CV contains the following information:

```json
{
  "nom": "Jean Dupont",
  "email": "jean.dupont@email.com",
  "telephone": "‪+33 6 12 34 56 78‬",
  "langue_cv": "fr",
  "specialité": "Développement Web",
  "competences": ["JavaScript", "React", "Node.js"],
  "annees_experience": 5,
  "projets_realises": 12,
  "diplome": "Master Informatique",
  "etablissement": "Université de Paris",
  "annee_obtention": 2018,
  "langues": ["Français", "Anglais"],
  "localisation": "Paris, France"
}
```

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/TuniHire-CV-Generator.git
   cd TuniHire-CV-Generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the script to generate 2000 CV profiles:

```bash
python cv_generator_simple.py
```

You can modify the number of CVs to generate by editing the script parameter:

```python
# Generate custom number of CVs
cvs = generate_cvs(5000)  # Change 5000 to your desired number
```

## 🛠️ Customization

The script contains several data arrays that you can modify to customize the generated CVs:

- `specialties`: Add or remove professional specializations
- `tech_skills`: Edit the list of technical skills
- `institutions`: Customize educational institutions
- `degree_types` and `degree_fields`: Modify education qualifications
- `cities`: Change location options

## 📊 Example Output

The script generates a `cvs_data.csv` file that can be opened in Excel, Google Sheets, or any CSV-compatible application. Each row contains a complete CV profile with all fields properly formatted.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by the needs of HR technology platforms
- Designed to provide realistic test data for recruitment systems

---

Created with ❤️ for TuniHire
