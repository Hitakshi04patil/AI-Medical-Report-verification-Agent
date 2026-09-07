# AI Medical Report Verification Agent

## Project Overview

The AI Medical Report Verification Agent is a Python-based application designed to verify employee medical fitness reports.

The system accepts a medical report in PDF format, reads and extracts the required information, performs different validations, and provides the final verification result through a Flask API.

## Key Features

* Upload medical report PDF
* Read and extract PDF content
* OCR support for scanned PDF pages
* Extract candidate details
* Verify candidate information
* Verify doctor signature and stamp
* Verify hospital details
* Validate report date
* Verify medical fitness information
* Generate overall report validation result
* Return verification results in JSON format
* API testing using Postman

## Project Flow

```text
Medical Report PDF
        ↓
PDF Upload
        ↓
Read PDF
        ↓
Extract Information
        ↓
Candidate Verification
        ↓
Doctor Verification
        ↓
Hospital Verification
        ↓
Report Validation
        ↓
Medical Verification
        ↓
Overall Validation
        ↓
JSON Response
```

## Technologies Used

* Python
* Flask
* PyMuPDF
* Tesseract OCR
* pytesseract
* Pillow
* Regular Expressions
* HTML
* CSS
* Postman

## Project Structure

```text
AI Medical Report Verification Agent
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── app.py
├── extract.py
├── verify.py
├── verification.py
├── medical_parameters.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

The project uses the following Python libraries:

```text
Flask
PyMuPDF
pytesseract
Pillow
```

Tesseract OCR also needs to be installed separately on the system for OCR-based PDF processing.

## How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open the Application

```text
http://127.0.0.1:5000/
```

## API Endpoint

```text
POST /upload
```

The `/upload` endpoint accepts a medical report PDF and returns the verification result in JSON format.

## API Testing Using Postman

The Flask API was tested using Postman.

### Request Details

**Method:**

```text
POST
```

**Endpoint:**

```text
http://127.0.0.1:5000/upload
```

### Body

Select:

```text
form-data
```

Add the following field:

```text
Key: file
Type: File
Value: Select Medical Report PDF
```

The uploaded medical report is processed by the Flask API, and the verification result is returned in JSON format.

## Verification

The system performs verification for:

* Candidate Details
* Doctor Details
* Hospital Details
* Medical Report
* Medical Fitness
* Overall Report

## Future Improvements

* Database integration
* Medical report history
* Search and filter functionality
* Dashboard
* Improved PDF extraction
* Improved OCR accuracy
* Support for different medical report formats

## Author

Hitakshi Patil
