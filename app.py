from flask import Flask, request, jsonify, render_template
import json
import re
import logging  # For error logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the drug database with error handling
def load_drugs():
    try:
        with open('drugs.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("drugs.json file not found. Please ensure it exists.")
        return []  # Return empty list to avoid crashes
    except json.JSONDecodeError:
        logging.error("Error decoding drugs.json. Check the file format.")
        return []

drugs_db = load_drugs()  # Load once and cache
drug_dict = {drug['generic_name'].lower(): drug for drug in drugs_db if 'generic_name' in drug}  # Quick lookup, skip invalid entries

# Rule-based interaction checker
def check_interactions(drug_names):
    interactions = []
    for i in range(len(drug_names)):
        for j in range(i + 1, len(drug_names)):
            drug1 = drug_names[i].lower()
            drug2 = drug_names[j].lower()
            if drug1 in drug_dict and drug2 in drug_dict:
                drug1_data = drug_dict[drug1]
                drug2_data = drug_dict[drug2]
                # Check direct interactions
                if drug2.title() in drug1_data.get('interactions', []) or drug1.title() in drug2_data.get('interactions', []):
                    interactions.append({
                        'pair': f"{drug1.title()} + {drug2.title()}",
                        'type': 'dangerous',
                        'reason': 'Known dangerous interaction (e.g., increased bleeding risk)'
                    })
                # Check same drug class
                elif drug1_data.get('drug_class') == drug2_data.get('drug_class'):
                    interactions.append({
                        'pair': f"{drug1.title()} + {drug2.title()}",
                        'type': 'caution',
                        'reason': 'Same drug class - potential overlap or reduced efficacy'
                    })
                else:
                    interactions.append({
                        'pair': f"{drug1.title()} + {drug2.title()}",
                        'type': 'safe',
                        'reason': 'No known interaction detected'
                    })
            else:
                interactions.append({
                    'pair': f"{drug1.title()} + {drug2.title()}",
                    'type': 'caution',
                    'reason': 'One or both drugs not in database - consult a doctor'
                })
    return interactions

# Dosage validation function with improved parsing
def validate_dosage(drug_name, dose, age):
    if drug_name.lower() not in drug_dict:
        return {'valid': True, 'warning': 'Drug not in database', 'color': 'yellow'}
    
    drug = drug_dict[drug_name.lower()]
    max_dose_str = drug.get('max_dose', 'Unknown')  # Fallback if missing
    
    # Parse dose input (e.g., "500 mg" -> 500)
    dose_num_match = re.search(r'(\d+)', dose)
    if not dose_num_match:
        return {'valid': False, 'warning': 'Invalid dose format', 'color': 'red'}
    dose_num = int(dose_num_match.group(1))
    
    # Parse max_dose (e.g., "4000 mg per day" -> 4000)
    max_dose_match = re.search(r'(\d+)', max_dose_str)
    max_num = int(max_dose_match.group(1)) if max_dose_match else 0  # Default to 0 if parsing fails
    
    # Age restriction check
    age_restr = drug.get('age_restrictions', '').lower()
    if 'under' in age_restr:
        age_limit_match = re.search(r'under (\d+)', age_restr)
        if age_limit_match and age < int(age_limit_match.group(1)):
            return {'valid': False, 'warning': f'Not recommended for age {age}', 'color': 'red'}
    elif 'over' in age_restr:
        age_limit_match = re.search(r'over (\d+)', age_restr)
        if age_limit_match and age > int(age_limit_match.group(1)):
            return {'valid': True, 'warning': 'Use with caution for older age', 'color': 'yellow'}
    
    # Elderly high-dose warning
    if age > 65 and dose_num > (max_num * 0.5):
        return {'valid': True, 'warning': 'High dose for elderly - monitor closely', 'color': 'yellow'}
    
    valid = dose_num <= max_num
    color = 'green' if valid else 'red'
    warning = 'Safe dose' if valid else f'Dose exceeds maximum ({max_dose_str})'
    
    return {'valid': valid, 'warning': warning, 'color': color}

# Generic substitution finder
def suggest_generics(drug_name):
    if drug_name.lower() not in drug_dict:
        return []
    
    drug = drug_dict[drug_name.lower()]
    drug_class = drug.get('drug_class', '')
    price = drug.get('price', 0)  # Fallback if price is missing
    
    alternatives = []
    for other_drug in drugs_db:
        if (other_drug.get('drug_class') == drug_class and 
            other_drug.get('generic_name', '').lower() != drug_name.lower() and 
            other_drug.get('price', float('inf')) < price):
            alternatives.append({
                'name': other_drug.get('generic_name', 'Unknown'),
                'price': other_drug.get('price', 0),
                'savings': price - other_drug.get('price', 0)
            })
    
    return sorted(alternatives, key=lambda x: x['savings'], reverse=True)[:3]  # Top 3

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')  # Assumes index.html is in templates folder

@app.route('/check', methods=['POST'])
def check_medications():
    try:
        data = request.json
        drug_names = data.get('drugs', [])  # List of drugs
        age = data.get('age')  # Integer age
        doses = data.get('doses', [])  # List of doses
        
        # Input validation
        if not isinstance(drug_names, list) or len(drug_names) < 2:
            return jsonify({'error': 'At least 2 drugs are required'}), 400
        if not isinstance(age, int) or age < 0:
            return jsonify({'error': 'Invalid age'}), 400
        if len(doses) != len(drug_names):
            return jsonify({'error': 'Doses must match the number of drugs'}), 400
        
        interactions = check_interactions(drug_names)
        validations = [validate_dosage(drug, doses[i] if i < len(doses) else 'Unknown', age) for i, drug in enumerate(drug_names)]
        generics = [suggest_generics(drug) for drug in drug_names]
        
        return jsonify({
            'interactions': interactions,
            'validations': validations,
            'generics': generics,
            'age': age
        })
    except Exception as e:
        logging.error(f"Error in /check endpoint: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
