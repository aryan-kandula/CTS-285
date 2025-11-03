# Datamon Answer Checker (Flask Web App)

## Overview
This project converts the console-based Datamon Checker into a simple Flask web app.  
It allows users to input a Datamon and an Answer, then verifies correctness in the browser.

## Framework Used
**Flask** — A lightweight Python web framework used to build small web applications with HTML templates.

---

## Installation
Before running the project, install Flask on your computer.

### Step 1 — Open Terminal
Open the terminal inside VS Code (bottom panel) or use Command Prompt.

### Step 2 — Run This Command
pip install flask

yaml
Copy code

*(“pip” is Python’s package manager — this command installs Flask.)*

---

## How to Run
After installation:

1. In VS Code terminal, make sure you are inside the folder  
   `ORANGE-01-aryankandula`
2. Run the Python file:
python app.py

less
Copy code
3. When you see:
Running on http://127.0.0.1:5000/

yaml
Copy code
open your web browser and visit that address.

4. You’ll see the web interface.  
Enter a Datamon and its Answer, then click **Check**.

---

## Features
- Compares Datamon and Answer (case-insensitive)
- Displays colored feedback:
- ✅ Green — Correct  
- ❌ Red — Incorrect  
- ⚠️ Orange — Missing input  
- Reset button for quick reuse
- Clean and centered design

---

## Example
**Input:**  
Datamon → Pikachu  
Answer → Pikachu  

**Output:**  
✅ Correct!

**Input:**  
Datamon → Pikachu  
Answer → Charmander  

**Output:**  
❌ Incorrect!

---

## Known Limitations
- Only string comparison (no external data)
- Runs locally (not hosted online)

---

## Author
**Aryan Kandula**  
CTS-285 — ORANGE-01 Web Interface Deployment