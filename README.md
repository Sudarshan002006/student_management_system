# Student Grade Management System

A beginner-friendly web app built with **Python (Flask)** and **HTML + CSS**.
Student data is stored in a Python list in memory while the app runs — no
database and no extra libraries.

## Features

- Add a student (name, roll number, class) and marks for 5 subjects.
- Validation: required fields, unique roll number, marks must be 0–100.
- Automatic report card with total, percentage, grade and Pass/Fail status.
- All-students table with live search by name or roll number.
- Class statistics: topper, average, highest/lowest percentage, pass/fail counts.

## File structure

```
project/
  app.py                 # Flask backend (all Python logic)
  requirements.txt       # Flask
  templates/
    base.html            # Layout: navbar, flash messages, footer
    index.html           # Home / Add Student form
    result.html          # Report card
    students.html        # All students table + search
    stats.html           # Class statistics
  static/
    style.css            # Responsive styling
```

## Design system

The UI follows the **Flat Design** style from the
[UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) skill:

- Solid education-teal palette (`#0F766E` primary, `#D97706` accent) — no gradients or shadows
- Plus Jakarta Sans typography
- Inline SVG icons (no emoji icons), 150–200 ms hover transitions
- Visible focus states, `prefers-reduced-motion` support, skip link, ARIA labels
- Responsive at 375 / 768 / 1024 / 1440 px

## How to run

1. Install Python 3.10+ from <https://python.org> if needed.
2. Open a terminal in this folder and install Flask:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:

   ```bash
   python app.py
   ```

4. Open your browser at <http://127.0.0.1:5000>

> Data is kept in memory. Restarting the server clears all students.

## Grading rules

| Item   | Rule                                             |
| ------ | ------------------------------------------------ |
| Total  | Sum of 5 subjects (out of 500)                   |
| Percentage | (total / 500) × 100                          |
| Grade  | A+ ≥ 90, A 80–89, B 70–79, C 60–69, D 50–59, F < 50 |
| Status | Fail if any subject is below 35, otherwise Pass   |

## Python concepts used

| Concept              | Where in `app.py`                                                        |
| -------------------- | ------------------------------------------------------------------------ |
| Variables / types    | `SUBJECTS`, `MAX_MARKS_PER_SUBJECT`, `students`, student dictionaries    |
| Input                | `request.form` (add form), `request.args` (search box)                    |
| Output               | `render_template(...)`, `flash(...)`, `redirect(...)`                     |
| Operators            | `+`, `/`, `*`, `round()`, `>`, `<`, `>=`, `==`, `or`, `and` (via `elif`)  |
| if / elif / else     | `find_grade()`, validation in `index()`                                  |
| Lists                | `students` (all students), `marks` (one student's marks), `errors`        |
| Loops                | `for` in totals/status/stats, `while` in `roll_number_exists()`          |
| Functions            | `calculate_total`, `calculate_percentage`, `find_grade`, `find_status`, `validate_marks`, `get_class_statistics`, helpers |

## Ideas to extend

1. **Database storage** — save students in SQLite/CSV so data survives restarts.
2. **Teacher login** — add sessions and protect the add/delete pages.
3. **PDF report card** — generate and download a printable PDF per student.
