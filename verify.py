import re
from datetime import datetime

def extract_candidate_details(pdf_text):

    candidate = {}

    # Candidate Name
    name_match = re.search(
        r"Name of the Candidate\s*([A-Za-z ]+)",
        pdf_text,
        re.IGNORECASE
    )

    if name_match:
        candidate["Candidate Name"] = " ".join(name_match.group(1).split())
    else:
        candidate["Candidate Name"] = "Not Found"

    # Age
    age_match = re.search(
        r"Age\s*[:/]?\s*(\d+)",
        pdf_text,
        re.IGNORECASE
    )

    if age_match:
        candidate["Age"] = age_match.group(1)
    else:
        candidate["Age"] = "Not Found"

    # Gender
    gender_match = re.search(
        r"\b(Male|Female)\b",
        pdf_text,
        re.IGNORECASE
    )

    if gender_match:
        candidate["Gender"] = gender_match.group(1).title()
    else:
        candidate["Gender"] = "Not Found"

    # Fitness Status
    if "Temporarily Unfit" in pdf_text:
        candidate["Fitness Status"] = "Temporary Unfit"

    elif "Unfit" in pdf_text:
        candidate["Fitness Status"] = "UNFIT"

    elif "Fit" in pdf_text:
        candidate["Fitness Status"] = "FIT"

    else:
        candidate["Fitness Status"] = "Not Found"

    return candidate


def verify_candidate(candidate, pdf_text, photo_present):

    result = {}

    # Candidate Name
    if candidate["Candidate Name"] != "Not Found":
        result["Candidate Name"] = "Verified"
    else:
        result["Candidate Name"] = "Missing"

    # Age
    if candidate["Age"] != "Not Found":
        result["Age"] = "Verified"
    else:
        result["Age"] = "Missing"

    # Gender
    if candidate["Gender"] != "Not Found":
        result["Gender"] = "Verified"
    else:
        result["Gender"] = "Missing"

    # Fitness Status
    if candidate["Fitness Status"] != "Not Found":
        result["Fitness Status"] = candidate["Fitness Status"]
    else:
        result["Fitness Status"] = "Missing"

    # Candidate Photo

    if photo_present:
       result["Candidate Photo"] = "Present"
    else:
        result["Candidate Photo"] = "Missing"

    return result

# -----------------------------
# Doctor Verification
# -----------------------------

def verify_doctor(pdf_text):

    doctor = {}

    # Doctor Signature
    if "Signature" in pdf_text:
        doctor["Doctor Signature"] = "Present"
    else:
        doctor["Doctor Signature"] = "Missing"

    # Doctor Stamp
    if "Medical Registration" in pdf_text or "Registration No" in pdf_text:
        doctor["Doctor Stamp"] = "Present"
    else:
        doctor["Doctor Stamp"] = "Missing"

    # Doctor Specialization
    if "Eye Examination" in pdf_text or "Eye Specialist" in pdf_text or "Ophthalmology" in pdf_text:
        doctor["Doctor Specialization"] = "Eye Specialist"

    elif "ECG" in pdf_text:
        doctor["Doctor Specialization"] = "Physician"

    elif "Chest X" in pdf_text or "CHEST PA" in pdf_text.upper():
        doctor["Doctor Specialization"] = "Radiologist"

    else:
        doctor["Doctor Specialization"] = "General Physician"

    return doctor


# Hospital Verification
# -----------------------------
def verify_hospital(pdf_text):

    hospital = {}

    # Hospital Name
    if (
        "HOSPITAL" in pdf_text.upper()
        or "LAB" in pdf_text.upper()
        or "DIAGNOSTIC" in pdf_text.upper()
        or "MEDICAL" in pdf_text.upper()
        or "CLINIC" in pdf_text.upper()
    ):
        hospital["Hospital Name"] = "Verified"
    else:
        hospital["Hospital Name"] = "Missing"

    # Hospital Logo
    if "LOGO" in pdf_text.upper():
        hospital["Hospital Logo"] = "Present"
    else:
        hospital["Hospital Logo"] = "Not Verified"

    return hospital

# -----------------------------
# Report Validation
# -----------------------------
def verify_report(pdf_text):

    report = {}

    # -----------------------------
    # Report Date
    # -----------------------------
    date_match = re.search(r"(\d{2})[-/](\d{2})[-/](\d{4})", pdf_text)

    if date_match:

        report_date = date_match.group(0)
        report["Report Date"] = report_date

        try:
            report_dt = datetime.strptime(report_date, "%d-%m-%Y")
            today = datetime.today()

            # Report is valid for 1 year
            expiry_dt = report_dt.replace(
                year=report_dt.year + 1
            )

            if today <= expiry_dt:
                report["Report Expiry"] = "Valid"
            else:
                report["Report Expiry"] = "Expired"

        except:
            report["Report Expiry"] = "Unknown"

    else:
        report["Report Date"] = "Missing"
        report["Report Expiry"] = "Unknown"

    # -----------------------------
    # Report Type
    # -----------------------------
    if "Eye Examination" in pdf_text or "Eye Specialist" in pdf_text:
        report["Report Type"] = "Eye Medical Report"

    elif "Chest X Ray" in pdf_text or "CHEST PA" in pdf_text.upper():
        report["Report Type"] = "Chest X-Ray Report"

    elif "ECG" in pdf_text.upper():
        report["Report Type"] = "ECG Report"

    else:
        report["Report Type"] = "Medical Report"

    return report
def verify_medical(pdf_text):

    medical = {}

    # Fitness Status
    if "Temporarily Unfit" in pdf_text:
        medical["Fitness Status"] = "Temporary Unfit"

    elif "Unfit" in pdf_text:
        medical["Fitness Status"] = "UNFIT"

    elif "Fit" in pdf_text:
        medical["Fitness Status"] = "FIT"

    else:
        medical["Fitness Status"] = "Missing"

   
   # Checkbox Validation
    status = medical["Fitness Status"]

    if status in ["FIT", "UNFIT", "Temporary Unfit"]:
        medical["Checkbox Validation"] = "Correct"
    else:
          medical["Checkbox Validation"] = "Incorrect"

    return medical

# -----------------------------
# Overall Report Validation
# -----------------------------

def verify_overall(candidate, doctor, hospital, report, medical):

    overall = {}

    reasons = []

    # -----------------------------
    # Candidate Verification
    # -----------------------------

    if candidate["Candidate Name"] == "Missing":
        reasons.append("Candidate Name Missing")

    if candidate["Age"] == "Missing":
        reasons.append("Age Missing")

    if candidate["Gender"] == "Missing":
        reasons.append("Gender Missing")

    if candidate["Candidate Photo"] == "Missing":
        reasons.append("Candidate Photo Missing")

    # -----------------------------
    # Doctor Verification
    # -----------------------------

    if doctor["Doctor Signature"] == "Missing":
        reasons.append("Doctor Signature Missing")

    if doctor["Doctor Stamp"] == "Missing":
        reasons.append("Doctor Stamp Missing")

    # -----------------------------
    # Report Validation
    # -----------------------------

    if report["Report Date"] == "Missing":
        reasons.append("Report Date Missing")

    if report["Report Expiry"] == "Expired":
        reasons.append("Report Expired")

    # -----------------------------
    # Medical Validation
    # -----------------------------

    if medical["Checkbox Validation"] == "Incorrect":
        reasons.append("Fitness Status Validation Failed")

    # -----------------------------
    # Final Decision
    # -----------------------------

    if len(reasons) == 0:

        overall["Overall Status"] = "VALID REPORT"
        overall["Reason"] = "None"

    else:

        overall["Overall Status"] = "INVALID REPORT"
        overall["Reason"] = reasons

    return overall
