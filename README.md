# MANBHUM VICTORIA INSTITUTION — Student Grade Management System

A beginner-friendly Flask web application for recording student marks, calculating totals/percentages/grades, and generating report cards. No database required — data is stored in a Python list while the app runs.

---

## 📁 File Organization

```
IT MINI PROJECT/
├── RUN_WEBSITE.bat          <-- DOUBLE-CLICK THIS to start the website
├── INSTALL_FLASK.bat         <-- Run this first if Flask is not installed
├── app.py                    <-- Flask backend (all Python logic)
├── requirements.txt          <-- Python dependencies
├── README.md                 <-- This file
├── .gitignore                <-- Git ignore rules
├── .git/                     <-- Git version control folder
├── __pycache__/              <-- Python cache (auto-generated)
├── templates/                <-- HTML page templates
│   ├── base.html             <-- Base layout (navbar, footer, flash messages)
│   ├── index.html            <-- Add Student form page
│   ├── result.html           <-- Individual report card page
│   ├── students.html         <-- All students table + search + filters
│   ├── stats.html            <-- Class summary dashboard
│   └── _radar_chart.html     <-- Radar chart component (included in stats)
└── static/                   <-- CSS, images, etc.
    └── style.css             <-- All styling (school colors, report card layout)
```

---

## 🚀 How to Run (Double-Click Method)

### First-time setup only:
1. **Double-click `INSTALL_FLASK.bat`** — This installs Flask (only needed once).

### Every time you want to use the website:
1. **Double-click `RUN_WEBSITE.bat`** — This starts the server and opens your browser automatically.
2. The website opens at: **http://127.0.0.1:5000**
3. From another device on the same Wi-Fi: **http://10.183.219.135:5000**

### Manual method (if .bat files don't work):
```powershell
cd "C:\Users\Sudarshan\Desktop\IT MINI PROJECT"
python app.py
```
Then open your browser to `http://127.0.0.1:5000`

---

## 📄 Pages & Features

| Page | URL | What it does |
|------|-----|--------------|
| **Add Student** | `/` | Form to enter student name, roll number, class, and 5 subject marks |
| **Report Card** | `/result/<roll>` | Individual marksheet with total, percentage, grade, pass/fail stamp |
| **All Results** | `/students` | Searchable table of all students with View/PDF buttons |
| **Class Summary** | `/stats` | Class statistics, subject averages, class-wise comparison |

---

## 🎯 Grading Logic

- **Total** = Sum of 5 subjects (out of 500)
- **Percentage** = (Total / 500) × 100
- **Grade**: A+ (≥90), A (80–89), B (70–79), C (60–69), D (50–59), F (<50)
- **Status**: FAIL if any subject is below 35, otherwise PASS

---

## 🔑 Python Concepts Used (in `app.py`)

| Concept | Where it's used |
|---------|----------------|
| **Variables & Data Types** | `SUBJECTS`, `students` list, integers, strings, floats |
| **Input** | `request.form.get()` from HTML form; `request.args.get()` for search |
| **Output** | `render_template()` sends data to HTML pages; `flash()` shows messages |
| **Operators** | `+`, `/`, `*`, `==`, `<`, `>=`, `or`, `and` |
| **if / elif / else** | `find_grade()` function, validation checks |
| **Lists** | `students` (all records), `marks` (5 subjects per student), `errors` |
| **Loops** | `for` loops for totals/stats; `while` loop for roll number validation |
| **Functions** | `calculate_total()`, `calculate_percentage()`, `find_grade()`, `find_status()`, `validate_marks()`, `get_class_statistics()` |

---

## 🛡️ Validation Rules

- Student name, roll number, and class are required
- Roll numbers must be unique (duplicate check with while loop)
- Marks must be whole numbers between 0 and 100
- Pass mark is 35 in every subject

---

## 📊 Sample Data

The app comes pre-loaded with 8 sample students (Indian names, varied marks, mix of pass/fail) so you can see the system working immediately.

---

## 🖨️ Print / PDF

- Each report card has a **"Print Report Card"** button
- Clicking it generates a downloadable PDF using only Python's standard library (no extra packages needed)

---

## 📮 School Identity

- **School**: MANBHUM VICTORIA INSTITUTION
- **Department**: Examination Cell
- **Academic Year**: 2026–27
- **Exam**: Half-Yearly Examination
- **Contact**: examcell@mvi.edu.in

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Flask not found" | Double-click `INSTALL_FLASK.bat` first |
| Port already in use | Close other Python apps, or run `taskkill /F /IM python.exe` then try again |
| Website shows plain text | Make sure `static/style.css` exists and the server is running properly |
| Other devices can't connect | Use `http://10.183.219.135:5000` and ensure Windows Firewall allows port 5000 |

---

## 📤 To Push to GitHub (Sudarshan002006)

1. Create repo at https://github.com/New — name: `student-grade-management-system` (no README)
2. In PowerShell inside this folder:
   ```powershell
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/Sudarshan002006/student-grade-management-system.git
   git push -u origin main
   ```
