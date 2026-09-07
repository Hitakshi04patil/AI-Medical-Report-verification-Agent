import re

def extract_medical_parameters(pdf_text):

    parameters = {}

    # Blood Pressure
    bp = re.search(r'(\d{2,3}/\d{2,3})', pdf_text)
    parameters["Blood Pressure"] = bp.group(1) if bp else "Not Found"

    # Blood Sugar
    sugar = re.search(r'Blood Sugar.*?(\d+)', pdf_text, re.IGNORECASE)
    parameters["Blood Sugar"] = sugar.group(1) if sugar else "Not Found"

    # Hemoglobin
    hb = re.search(r'Haemoglobin.*?(\d+\.?\d*)', pdf_text, re.IGNORECASE)
    parameters["Haemoglobin"] = hb.group(1) if hb else "Not Found"

    # Vision
    if "6/6" in pdf_text:
        parameters["Vision"] = "6/6"
    else:
        parameters["Vision"] = "Not Found"

    # Colour Vision
    if "Colour Vision" in pdf_text:
        parameters["Colour Vision"] = "Present"
    else:
        parameters["Colour Vision"] = "Not Found"

    # Hearing
    if "Hearing" in pdf_text:
        parameters["Hearing"] = "Present"
    else:
        parameters["Hearing"] = "Not Found"

    # ECG
    if "ECG" in pdf_text.upper():
        parameters["ECG"] = "Present"
    else:
        parameters["ECG"] = "Not Found"

    # X-Ray
    if "X-RAY" in pdf_text.upper() or "XRAY" in pdf_text.upper():
        parameters["X-Ray"] = "Present"
    else:
        parameters["X-Ray"] = "Not Found"

    return parameters