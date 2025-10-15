# 💊 Medication Safety Checker

A web-based medication safety checker that allows users to search for drugs, view detailed information, and check for potential interactions — using a **local JSON database** with no backend or API required. Ideal for lightweight offline applications and rapid prototyping.

## 🚀 Key Features
- ✅ Search for medications by generic name
- 🧪 Detect potential drug interactions
- 🛡️ Display safety alerts, age restrictions, and dosage guidelines
- 💻 Render comprehensive drug information dynamically in the browser
- 🗃️ Fully offline: powered by a local JSON database (`medications.json`)
- ⚡ Minimal dependencies, lightweight, and fast

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Vanilla JS, ES6+)
- **Data Storage:** Local JSON file (`medications.json`)  
- **Data Structure:** Each medication object includes:
  - `generic_name`, `brand_names`, `drug_class`
  - `common_doses`, `max_dose`, `interactions`
  - `age_restrictions`, `side_effects`, `price`

## 📂 Project Structure
medication-safety-checker/
│
├─ index.html # Main UI
├─ script.js # Search logic and DOM rendering
├─ style.css # Optional styling
└─ medications.json # Local database of medications

## 💻 Usage
1. Open `index.html` in a modern browser.  
2. Type the medication name in the search box.  
3. Click **Search** to display full details:
   - Brand names, drug class, dosage
   - Maximum dose, interactions, age restrictions
   - Side effects and pricing  

Example search: `Aspirin`  

## 🔧 How It Works
- `script.js` loads `medications.json` via `fetch()`.  
- Searches the array of medication objects for a **case-insensitive match**.  
- Dynamically renders relevant details in the DOM without page reloads.  
- Fully modular — can easily integrate into frameworks or extend with new features.

## 🤝 Contributing
Contributions are welcome. You can:
- Add more medications to `medications.json`
- Improve search functionality (e.g., partial matches, autocomplete)
- Enhance UI/UX or add visualization features

## 📜 License
MIT License
