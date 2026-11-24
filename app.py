"""
Student Grade Management System
-------------------------------
A beginner-friendly Flask application.

Data storage: one Python list (`students`) kept in memory while the server
runs. No database and no extra libraries are used.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = "grade-manager-secret-key"

# ----------------------------------------------------------------------
# Constants (variables / data types: strings and integers)
# ----------------------------------------------------------------------
SUBJECTS = [
    {"name": "Maths", "field": "maths"},
    {"name": "Science", "field": "science"},
    {"name": "English", "field": "english"},
    {"name": "Social Studies", "field": "social_studies"},
    {"name": "Computer", "field": "computer"},
]

MAX_MARKS_PER_SUBJECT = 100                              # integer
PASS_MARK = 35                                           # integer
TOTAL_MAX_MARKS = MAX_MARKS_PER_SUBJECT * len(SUBJECTS)  # arithmetic operator *

# The in-memory "database": a LIST of dictionaries.
# Each dictionary stores one student's details, marks and results.
# Pre-seeded sample records for the Half-Yearly Examination 2026-27.
students = [
    {
        "name": "Aarav Sharma",
        "roll": "2026-014",
        "class": "10-A",
        "marks": [88, 92, 85, 78, 90],
        "total": 433,
        "percentage": 86.6,
        "grade": "A",
        "status": "Pass",
    },
    {
        "name": "Diya Verma",
        "roll": "2026-017",
        "class": "10-A",
        "marks": [94, 89, 91, 93, 88],
        "total": 455,
        "percentage": 91.0,
        "grade": "A+",
        "status": "Pass",
    },
    {
        "name": "Kabir Singh",
        "roll": "2026-021",
        "class": "10-B",
        "marks": [76, 70, 72, 68, 74],
        "total": 360,
        "percentage": 72.0,
        "grade": "B",
        "status": "Pass",
    },
    {
        "name": "Ananya Reddy",
        "roll": "2026-005",
        "class": "10-A",
        "marks": [90, 86, 88, 84, 92],
        "total": 440,
        "percentage": 88.0,
        "grade": "A",
        "status": "Pass",
    },
    {
        "name": "Rohan Mehta",
        "roll": "2026-029",
        "class": "10-B",
        "marks": [34, 52, 41, 38, 45],
        "total": 210,
        "percentage": 42.0,
        "grade": "F",
        "status": "Fail",
    },
    {
        "name": "Ishaan Kapoor",
        "roll": "2026-033",
        "class": "10-C",
        "marks": [65, 58, 60, 55, 62],
        "total": 300,
        "percentage": 60.0,
        "grade": "C",
        "status": "Pass",
    },
    {
        "name": "Sanya Pillai",
        "roll": "2026-011",
        "class": "10-C",
        "marks": [82, 79, 85, 80, 84],
        "total": 410,
        "percentage": 82.0,
        "grade": "A",
        "status": "Pass",
    },
    {
        "name": "Vihaan Joshi",
        "roll": "2026-040",
        "class": "10-B",
        "marks": [45, 39, 48, 42, 40],
        "total": 214,
        "percentage": 42.8,
        "grade": "F",
        "status": "Fail",
    },
]


# ----------------------------------------------------------------------
# Functions (each takes parameters and returns a value)
# ----------------------------------------------------------------------
def calculate_total(marks):
    """Add every mark in the list and return the total (for loop)."""
    total = 0
    for mark in marks:
        total = total + mark          # arithmetic operator +
    return total


def calculate_percentage(total, num_subjects):
    """Return the percentage rounded to 2 decimal places (arithmetic)."""
    if num_subjects <= 0:             # comparison operator <=
        return 0.0
    percentage = (total / (num_subjects * MAX_MARKS_PER_SUBJECT)) * 100
    return round(percentage, 2)


def find_grade(percentage):
    """Return a grade letter using if / elif / else (comparison operators)."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def find_status(marks):
    """Fail if ANY subject is below 35, otherwise Pass (loop + if)."""
    for mark in marks:
        if mark < PASS_MARK:          # comparison operator <
            return "Fail"
    return "Pass"


def validate_marks(raw_marks):
    """Return a list of error strings. An empty list means everything is valid."""
    errors = []
    for index in range(len(raw_marks)):
        raw_value = str(raw_marks[index]).strip()
        subject_name = SUBJECTS[index]["name"]

        if raw_value == "":           # comparison operator ==
            errors.append(subject_name + " marks are required.")
            continue

        try:
            mark = int(raw_value)
        except ValueError:
            errors.append(subject_name + " marks must be a whole number.")
            continue

        if mark < 0 or mark > MAX_MARKS_PER_SUBJECT:   # logical operator 'or'
            errors.append(
                subject_name
                + " marks must be between 0 and "
                + str(MAX_MARKS_PER_SUBJECT)
                + "."
            )
    return errors


def roll_number_exists(roll_number):
    """Check the list with a while loop (loop-based validation)."""
    roll_number = roll_number.strip().lower()
    index = 0
    while index < len(students):
        if students[index]["roll"].lower() == roll_number:
            return True
        index = index + 1
    return False


def build_student(name, roll_number, class_name, marks):
    """Create a student dictionary with all calculated results."""
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = find_grade(percentage)
    status = find_status(marks)

    return {
        "name": name.strip(),
        "roll": roll_number.strip(),
        "class": class_name.strip(),
        "marks": marks,          # a list stored inside a dictionary
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status,
    }


def find_student_by_roll(roll_number):
    """Return the student dictionary for a roll number, or None."""
    roll_number = roll_number.strip().lower()
    for student in students:
        if student["roll"].lower() == roll_number:
            return student
    return None


def get_class_statistics(student_list):
    """Return a dictionary of class-level statistics, or None if empty."""
    if len(student_list) == 0:
        return None

    total_percentage = 0.0
    passed = 0
    failed = 0
    highest = student_list[0]
    lowest = student_list[0]

    for student in student_list:
        total_percentage = total_percentage + student["percentage"]

        if student["percentage"] > highest["percentage"]:
            highest = student
        if student["percentage"] < lowest["percentage"]:
            lowest = student

        if student["status"] == "Pass":
            passed = passed + 1
        else:
            failed = failed + 1

    return {
        "count": len(student_list),
        "average": round(total_percentage / len(student_list), 2),
        "highest": highest,
        "lowest": lowest,
        "topper": highest,
        "passed": passed,
        "failed": failed,
    }


# Make the helper available inside templates (used by students.html).
app.jinja_env.globals["get_class_statistics"] = get_class_statistics


# ----------------------------------------------------------------------
# PDF report card (built with the Python standard library only)
# ----------------------------------------------------------------------
PDF_PAGE_WIDTH = 595.28   # A4 width in points
PDF_PAGE_HEIGHT = 841.89  # A4 height in points


def _pdf_escape(text):
    """Make text safe for a PDF literal string (latin-1 only)."""
    text = str(text).encode("latin-1", "replace").decode("latin-1")
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _pdf_text(x, y, text, font="F1", size=11, rgb=(0.06, 0.09, 0.16)):
    """Return a PDF text-drawing operation."""
    return "BT %.3f %.3f %.3f rg /%s %.2f Tf %.2f %.2f Td (%s) Tj ET" % (
        rgb[0], rgb[1], rgb[2], font, size, x, y, _pdf_escape(text),
    )


def _pdf_rect(x, y, box_width, box_height, rgb):
    """Return a PDF filled-rectangle operation."""
    return "%.3f %.3f %.3f rg %.2f %.2f %.2f %.2f re f" % (
        rgb[0], rgb[1], rgb[2], x, y, box_width, box_height,
    )


def _pdf_line(x1, y1, x2, y2, rgb, line_width=1):
    """Return a PDF line-drawing operation."""
    return "%.3f %.3f %.3f RG %.2f w %.2f %.2f m %.2f %.2f l S" % (
        rgb[0], rgb[1], rgb[2], line_width, x1, y1, x2, y2,
    )


def _pdf_text_width(text, size, bold=False):
    """Rough text width so short strings can be centred."""
    return len(str(text)) * size * (0.55 if bold else 0.5)


def generate_report_pdf(student):
    """Build a one-page PDF report card and return the raw bytes."""
    width = PDF_PAGE_WIDTH
    height = PDF_PAGE_HEIGHT
    margin = 48.0

    teal = (0.059, 0.463, 0.431)
    ink = (0.059, 0.090, 0.161)
    gray = (0.278, 0.333, 0.412)
    muted = (0.945, 0.961, 0.976)
    border = (0.886, 0.910, 0.937)
    white = (1.0, 1.0, 1.0)
    green = (0.086, 0.639, 0.290)
    red = (0.863, 0.149, 0.149)

    ops = []

    # ----- Header band -----
    ops.append(_pdf_rect(0, height - 96, width, 96, teal))
    ops.append(_pdf_text(margin, height - 40, "STUDENT GRADE MANAGEMENT SYSTEM", "F2", 9.5, white))
    ops.append(_pdf_text(margin, height - 72, "Report Card", "F2", 25, white))

    # ----- Student details -----
    details_y = height - 132
    ops.append(_pdf_text(margin, details_y, "STUDENT NAME", "F2", 8, gray))
    ops.append(_pdf_text(margin, details_y - 20, student["name"], "F2", 14, ink))

    ops.append(_pdf_text(margin + 210, details_y, "ROLL NUMBER", "F2", 8, gray))
    ops.append(_pdf_text(margin + 210, details_y - 20, student["roll"], "F1", 13, ink))

    ops.append(_pdf_text(margin + 330, details_y, "CLASS", "F2", 8, gray))
    ops.append(_pdf_text(margin + 330, details_y - 20, student["class"], "F1", 13, ink))

    # Status badge (top-right of the details block)
    status = student["status"]
    status_color = green if status == "Pass" else red
    badge_width, badge_height = 100.0, 30.0
    badge_x = width - margin - badge_width
    badge_y = details_y - 6
    ops.append(_pdf_rect(badge_x, badge_y, badge_width, badge_height, status_color))
    badge_label = "PASS" if status == "Pass" else "FAIL"
    badge_text_x = badge_x + (badge_width - _pdf_text_width(badge_label, 12, bold=True)) / 2
    ops.append(_pdf_text(badge_text_x, badge_y + 10, badge_label, "F2", 12, white))

    ops.append(_pdf_line(margin, details_y - 44, width - margin, details_y - 44, border, 1))

    # ----- Summary boxes -----
    summary = [
        ("TOTAL", "%d / 500" % student["total"], ink),
        ("PERCENTAGE", "%.2f%%" % student["percentage"], ink),
        ("GRADE", student["grade"], teal),
        ("STATUS", status, status_color),
    ]
    box_gap = 10.0
    box_width = (width - 2 * margin - 3 * box_gap) / 4
    box_height = 64.0
    box_y = height - 250          # bottom edge of the boxes
    for index, (label, value, color) in enumerate(summary):
        x = margin + index * (box_width + box_gap)
        ops.append(_pdf_rect(x, box_y, box_width, box_height, muted))
        ops.append(_pdf_text(x + 12, box_y + box_height - 20, label, "F2", 7.5, gray))
        ops.append(_pdf_text(x + 12, box_y + box_height - 46, value, "F2", 17, color))

    # ----- Marks table -----
    table_top = height - 274
    col_subject = margin
    col_marks = width - margin - 190
    col_max = width - margin - 110

    header_height = 24.0
    ops.append(_pdf_rect(margin, table_top - header_height, width - 2 * margin, header_height, muted))
    ops.append(_pdf_text(col_subject, table_top - 16, "Subject", "F2", 9.5, ink))
    ops.append(_pdf_text(col_marks, table_top - 16, "Marks", "F2", 9.5, ink))
    ops.append(_pdf_text(col_max, table_top - 16, "Max", "F2", 9.5, ink))

    row_height = 26.0
    for index, subject in enumerate(SUBJECTS):
        mark = student["marks"][index]
        row_y = table_top - header_height - (index + 1) * row_height
        ops.append(_pdf_text(col_subject, row_y + 8, subject["name"], "F1", 11, ink))
        mark_color = red if mark < PASS_MARK else ink
        ops.append(_pdf_text(col_marks, row_y + 8, str(mark), "F2", 11, mark_color))
        ops.append(_pdf_text(col_max, row_y + 8, "100", "F1", 11, gray))
        ops.append(_pdf_line(margin, row_y, width - margin, row_y, border, 1))

    # ----- Footer -----
    footer_y = table_top - header_height - 5 * row_height - 36
    ops.append(_pdf_line(margin, footer_y + 18, width - margin, footer_y + 18, border, 1))
    ops.append(_pdf_text(
        margin, footer_y,
        "Pass mark is 35 in every subject. Total is calculated out of 500.",
        "F1", 9, gray,
    ))
    generated = "Generated by Grade Manager"
    ops.append(_pdf_text(
        (width - _pdf_text_width(generated, 8.5)) / 2, 40, generated, "F1", 8.5, gray
    ))

    content = "\n".join(ops) + "\n"
    stream = content.encode("latin-1")

    # ----- Assemble the PDF objects -----
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        ("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.2f %.2f] "
         "/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>"
         % (width, height)).encode("latin-1"),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
        ("<< /Length %d >>\nstream\n" % len(stream)).encode("latin-1")
        + stream
        + b"\nendstream",
    ]

    pdf = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf += ("%d 0 obj\n" % number).encode("latin-1") + body + b"\nendobj\n"

    xref_start = len(pdf)
    pdf += ("xref\n0 %d\n" % (len(objects) + 1)).encode("latin-1")
    pdf += b"0000000000 65535 f \n"
    for offset in offsets:
        pdf += ("%010d 00000 n \n" % offset).encode("latin-1")
    pdf += ("trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n"
            % (len(objects) + 1, xref_start)).encode("latin-1")
    return bytes(pdf)


# ----------------------------------------------------------------------
# Routes: input (request.form / request.args) -> output (HTML pages)
# ----------------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # ----- INPUT: read the values sent by the HTML form -----
        name = request.form.get("name", "")
        roll_number = request.form.get("roll", "")
        class_name = request.form.get("class_name", "")

        raw_marks = []
        for subject in SUBJECTS:
            raw_marks.append(request.form.get(subject["field"], ""))

        # ----- VALIDATION -----
        errors = []

        if name.strip() == "":
            errors.append("Student name is required.")
        if roll_number.strip() == "":
            errors.append("Roll number is required.")
        elif roll_number_exists(roll_number):   # logical: only check when not empty
            errors.append(
                "Roll number '"
                + roll_number.strip()
                + "' already exists. Roll numbers must be unique."
            )
        if class_name.strip() == "":
            errors.append("Class is required.")

        errors.extend(validate_marks(raw_marks))

        # ----- OUTPUT: show friendly error messages on the form -----
        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "index.html", subjects=SUBJECTS, form=request.form, active_page="home"
            )

        # ----- Convert the validated text into integers -----
        marks = []
        for subject in SUBJECTS:
            marks.append(int(request.form.get(subject["field"], "0")))

        student = build_student(name, roll_number, class_name, marks)
        students.append(student)                 # store the student in the list

        flash("Result calculated for " + student["name"] + ".", "success")
        return redirect(url_for("result", roll=student["roll"]))

    # GET request: show an empty form
    return render_template("index.html", subjects=SUBJECTS, form={}, active_page="home")


@app.route("/result/<roll>")
def result(roll):
    student = find_student_by_roll(roll)
    if student is None:
        flash("Student with roll number '" + roll + "' was not found.", "error")
        return redirect(url_for("index"))

    # ----- OUTPUT: send the student's data to the report-card template -----
    return render_template(
        "result.html", student=student, subjects=SUBJECTS, active_page="result"
    )


@app.route("/report/<roll>/pdf")
def result_pdf(roll):
    student = find_student_by_roll(roll)
    if student is None:
        flash("Student with roll number '" + roll + "' was not found.", "error")
        return redirect(url_for("index"))

    pdf_data = generate_report_pdf(student)
    filename = "report-card-" + student["roll"].replace(" ", "_") + ".pdf"
    response = make_response(pdf_data)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=" + filename
    return response


@app.route("/students", endpoint="students")
def students_page():
    # ----- INPUT: the search box sends a query string -----
    query = request.args.get("q", "").strip().lower()

    if query == "":
        filtered = students
    else:
        filtered = []
        for student in students:                # loop + logical operator 'or'
            if query in student["name"].lower() or query in student["roll"].lower():
                filtered.append(student)

    return render_template(
        "students.html",
        students=filtered,
        query=request.args.get("q", ""),
        active_page="students",
    )


@app.route("/stats", endpoint="stats")
def stats_page():
    statistics = get_class_statistics(students)

    # ----- Subject-wise averages -----
    subject_averages = []
    if len(students) > 0:
        for index, subject in enumerate(SUBJECTS):
            total = 0
            for student in students:
                total = total + student["marks"][index]
            subject_averages.append({
                "name": subject["name"],
                "average": round(total / len(students), 1),
            })

    # ----- Class-wise breakdown -----
    class_breakdown = []
    class_names = sorted(set(student["class"] for student in students))
    for class_name in class_names:
        class_students = [s for s in students if s["class"] == class_name]
        class_total_pct = 0.0
        class_pass = 0
        for cs in class_students:
            class_total_pct = class_total_pct + cs["percentage"]
            if cs["status"] == "Pass":
                class_pass = class_pass + 1
        class_breakdown.append({
            "name": class_name,
            "count": len(class_students),
            "average": round(class_total_pct / len(class_students), 2),
            "passed": class_pass,
            "pass_pct": round(class_pass / len(class_students) * 100, 2),
        })

    return render_template(
        "stats.html",
        stats=statistics,
        subject_averages=subject_averages,
        class_breakdown=class_breakdown,
        active_page="stats",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
