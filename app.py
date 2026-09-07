from flask import Flask, request, jsonify,render_template
import os

from extract import extract_pdf_content

from verify import (
    extract_candidate_details,
    verify_candidate,
    verify_doctor,
    verify_hospital,
    verify_report,
    verify_medical,
    verify_overall
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload-page")
def upload_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Medical Report Upload</title>
    </head>

    <body>

        <h2>Employee Medical Fitness Management System</h2>

        <form action="/upload" method="POST" enctype="multipart/form-data">

            <input type="file" name="file" accept=".pdf" required>

            <br><br>

            <button type="submit">
                Verify Medical Report
            </button>

        </form>

    </body>
    </html>
    """

@app.route("/upload", methods=["POST"])
def upload_pdf():

    # Check PDF file
    if "file" not in request.files:
        return jsonify({
            "Error": "No file uploaded"
        })

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "Error": "No file selected"
        })

    # Save uploaded PDF
    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    # Extract PDF text
    pdf_text, photo_present = extract_pdf_content(filepath)

    # Candidate Verification
    candidate = extract_candidate_details(pdf_text)

    candidate_result = verify_candidate(
        candidate,
        pdf_text,
        photo_present
    )

    # Doctor Verification
    doctor_result = verify_doctor(pdf_text)

    # Hospital Verification
    hospital_result = verify_hospital(pdf_text)

    # Report Validation
    report_result = verify_report(pdf_text)

    # Medical Verification
    medical_result = verify_medical(pdf_text)

    # Overall Validation
    overall_result = verify_overall(
        candidate_result,
        doctor_result,
        hospital_result,
        report_result,
        medical_result
    )

    # Final JSON Response
    return jsonify({

        "Candidate Verification": candidate_result,

        "Doctor Verification": doctor_result,

        "Hospital Verification": hospital_result,

        "Report Validation": report_result,

        "Medical Verification": medical_result,

        "Overall Report Validation": overall_result

    })


if __name__ == "__main__":
    app.run(debug=True)