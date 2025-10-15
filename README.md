# 💊 Medication Safety Checker

A **rule-based** medication safety checker that helps users check for potential drug interactions, validate dosages, and find generic alternatives using a local drug database.

> ⚠️ **IMPORTANT DISCLAIMER**: This is an **educational tool only**. It is NOT a substitute for professional medical advice. Always consult a qualified healthcare provider before making any decisions about medications.

## 🎯 What This Tool Does

This web application allows users to:
- Check for potential interactions between multiple medications
- Validate dosages against maximum recommended limits
- Get age-specific warnings for medication use
- Find cheaper generic alternatives for prescribed drugs

## 🔍 How It Works

This checker uses **rule-based logic** with a local JSON database:

1. **Interaction Checking**: Compares drug pairs against a predefined list of known dangerous interactions
2. **Drug Class Analysis**: Identifies potential issues when drugs belong to the same class
3. **Dosage Validation**: Compares entered doses against maximum daily limits
4. **Age Restrictions**: Flags medications that may not be appropriate for certain age groups
5. **Generic Suggestions**: Finds cheaper alternatives within the same drug class

## 📋 Features

✅ **Drug Interaction Detection**
- Checks 2-3 medications at once
- Identifies dangerous, cautionary, and safe combinations
- Based on a curated database of 30 common medications

✅ **Dosage Validation**
- Validates doses against maximum daily limits
- Age-specific warnings for children and elderly
- Clear color-coded feedback (green/yellow/red)

✅ **Generic Alternatives**
- Suggests up to 3 cheaper alternatives
- Shows potential cost savings
- Filters by same drug class

✅ **User-Friendly Interface**
- Clean, responsive design
- Real-time validation
- Clear result presentation

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: Local JSON file
- **No external APIs or databases required**

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Flask

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Ajeema24434/medication-safety-checker.git
cd medication-safety-checker
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
medication-safety-checker/
├── app.py              # Flask backend with interaction/validation logic
├── drugs.json          # Local database of 30 medications
├── index.html          # Frontend interface
└── README.md           # This file
```

## 💊 Included Medications

The database includes 30 commonly prescribed medications across various categories:
- Pain relievers (Aspirin, Ibuprofen, Naproxen, Paracetamol)
- Antibiotics (Amoxicillin, Azithromycin, Ciprofloxacin)
- Cardiovascular drugs (Lisinopril, Atorvastatin, Metoprolol)
- Diabetes medications (Metformin, Insulin, Glipizide)
- Antidepressants (Sertraline, Escitalopram)
- And more...

## ⚠️ Limitations

This tool has significant limitations and should be understood clearly:

1. **Limited Database**: Only 30 medications included - not comprehensive
2. **Simplified Interactions**: Cannot detect all possible drug interactions
3. **No Medical Expertise**: Rule-based logic cannot replace pharmacist/doctor knowledge
4. **Static Data**: Information may become outdated and is not regularly updated
5. **No Personalization**: Cannot account for individual health conditions, allergies, or genetic factors
6. **Educational Purpose**: Designed for learning about drug safety concepts, not clinical use

## 🎓 Educational Use Cases

This project is suitable for:
- Learning about drug interactions and safety
- Understanding basic pharmacology concepts
- Web development practice (Flask + JavaScript)
- Database structure design for healthcare applications
- UI/UX design for medical tools

## 🤝 Contributing

Contributions are welcome! However, please note:
- All drug information must be verified against reliable sources
- Medical accuracy is critical - cite sources for any additions
- Maintain the educational disclaimer prominently

## 📝 License

This project is open source and available for educational purposes.

## 📞 Support

If you find bugs or have suggestions, please open an issue on GitHub.

---

**Remember**: This is a learning project. For real medication questions, always consult qualified healthcare professionals including doctors, pharmacists, or clinical pharmacists.

## 🔗 Resources for Accurate Drug Information

For reliable, professional drug information, consult:
- [Drugs.com](https://www.drugs.com/)
- [MedlinePlus](https://medlineplus.gov/)
- [FDA Drug Information](https://www.fda.gov/drugs)
- Your local pharmacist or healthcare provider
