# AI Medical Report Verification Agent

A Python Flask-based application for verifying employee medical reports and extracting important information from PDF medical documents.

## 📌 Project Overview

The **AI Medical Report Verification Agent** processes employee medical report PDFs and performs multiple verification checks.

The system extracts candidate information, verifies medical report details, checks doctor and hospital information, validates the report date, and generates an overall verification result.

The application provides the final result through a **Flask REST API** in JSON format.

## ✨ Key Features

* 📄 Medical report PDF upload
* 🔍 PDF text extraction using PyMuPDF
* 🖼️ OCR support for scanned PDF reports
* 👤 Candidate details extraction
* 🩺 Medical information extraction
* 👨‍⚕️ Doctor signature and stamp verification
* 🏥 Hospital details verification
* 📅 Medical report date validation
* ✅ Medical fitness verification
* 📊 Overall report validation
* 🔗 Flask REST API
* 🧪 API testing using Postman
* 📦 JSON response

## 🔄 Project Flow

```text
Medical Report PDF
        ↓
PDF Upload
        ↓
PDF Text Extraction
        ↓
OCR if Required
        ↓
Candidate Details Extraction
        ↓
Doctor Verification
        ↓
Hospital Verification
        ↓
Report Date Validation
        ↓
Medical Fitness Verification
        ↓
Overall Validation
        ↓
JSON API Response
```

## 🛠️ Technologies Used

| Technology          | Purpose                      |
| ------------------- | ---------------------------- |
| Python              | Application development      |
| Flask               | REST API and web application |
| PyMuPDF             | PDF text extraction          |
| Tesseract OCR       | Scanned PDF processing       |
| pytesseract         | Python OCR integration       |
| Pillow              | Image processing             |
| Regular Expressions | Information extraction       |
| HTML                | Frontend                     |
| CSS                 | User interface               |
| Postman             | API testing                  |

## 📁 Project Structure

```text
AI-Medical-Report-Verification-Agent
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── extract.py
├── verify.py
├── medical_parameters.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Hitakshi04patil/AI-Medical-Report-Verification-Agent.git
```

### 2. Open the Project

```bash
cd AI-Medical-Report-Verification-Agent
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000/
```

## 🔌 API Endpoint

### Upload Medical Report

**Method:**

```text
POST
```

**Endpoint:**

```text
/upload
```

The API accepts a medical report PDF and returns the verification result in JSON format.

## 🧪 API Testing with Postman

The API was tested using Postman.

### Request

```text
POST http://127.0.0.1:5000/upload
```

### Body

Select:

```text
form-data
```

Add:

```text
Key: file
Type: File
Value: Select Medical Report PDF
```

The API processes the uploaded report and returns the verification result in JSON format.

## 🔎 Verification Checks

The system currently performs verification for:

* Candidate details
* Doctor details
* Hospital details
* Medical report information
* Report date
* Medical fitness information
* Overall report status

## 📋 Example API Response

```json
{
    "candidate": {
        "name": "Candidate Name",
        "age": "25",
        "gender": "Male"
    },
    "verification": {
        "candidate": "Valid",
        "doctor": "Valid",
        "hospital": "Valid",
        "report": "Valid",
        "medical": "Valid",
        "overall": "Valid"
    }
}
```

## 🚀 Future Improvements

* Database integration
* Medical report history
* Search and filter functionality
* Dashboard and analytics
* Improved OCR accuracy
* Support for multiple medical report formats
* Authentication and role-based access
* Improved hospital logo verification

## 🔐 Security & Privacy

Medical reports may contain sensitive personal and health information.

For this reason, actual medical report PDFs and sensitive files are **not included in this GitHub repository**.

## 👩‍💻 Author

**Hitakshi Patil**

GitHub: Hitakshi04patil
