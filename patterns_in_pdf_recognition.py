# patterns_in_pdf_recognition.py

import re

# Define all possible patterns for sensitive data
patterns = {
    'Full Name': r'Full Name:\s*([^\n]*)|Name:\s*([^\n]*)',
    'Date of Birth': r'Date of Birth:\s*([^\n]*)|DOB:\s*([^\n]*)|Birth Date:\s*([^\n]*)',
    'Social Security Number': r'Social Security Number:\s*([^\n]*)|SSN:\s*([^\n]*)',
    'Address': r'Address:\s*([^\n]*)',
    'Phone Number': r'Phone Number:\s*([^\n]*)|Phone:\s*([^\n]*)|Contact:\s*([^\n]*)',
    'Email Address': r'Email Address:\s*([^\n]*)|Email:\s*([^\n]*)',
    'Bank Name': r'Bank Name:\s*([^\n]*)',
    'Account Number': r'Account Number:\s*([^\n]*)|Account No:\s*([^\n]*)',
    'Routing Number': r'Routing Number:\s*([^\n]*)|Routing No:\s*([^\n]*)',
    'Credit Card Number': r'Credit Card Number:\s*([^\n]*)|CC Number:\s*([^\n]*)',
    'Expiration Date': r'Expiration Date:\s*([^\n]*)|Exp Date:\s*([^\n]*)',
    'CVV': r'CVV:\s*([^\n]*)|Security Code:\s*([^\n]*)',
    'Health Insurance Provider': r'Health Insurance Provider:\s*([^\n]*)|Insurance Provider:\s*([^\n]*)',
    'Policy Number': r'Policy Number:\s*([^\n]*)|Policy No:\s*([^\n]*)',
    'Primary Care Physician': r'Primary Care Physician:\s*([^\n]*)|PCP:\s*([^\n]*)|Physician:\s*([^\n]*)',
    'Medical Conditions': r'Medical Conditions:\s*([^\n]*)|Conditions:\s*([^\n]*)',
    'Current Medications': r'Current Medications:\s*([^\n]*)|Medications:\s*([^\n]*)',
    'Employer': r'Employer:\s*([^\n]*)|Company:\s*([^\n]*)',
    'Job Title': r'Job Title:\s*([^\n]*)|Title:\s*([^\n]*)|Position:\s*([^\n]*)',
    'Employee ID': r'Employee ID:\s*([^\n]*)|ID Number:\s*([^\n]*)',
    'Department': r'Department:\s*([^\n]*)|Dept:\s*([^\n]*)',
    'Work Email': r'Work Email:\s*([^\n]*)|Work E-mail:\s*([^\n]*)|Business Email:\s*([^\n]*)',
    'Work Phone': r'Work Phone:\s*([^\n]*)|Business Phone:\s*([^\n]*)|Office Phone:\s*([^\n]*)'
}

def extract_sensitive_info(text):
    extracted_info = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted_info[key] = match.group(1) or match.group(2)  # Adjust to match the correct group
    return extracted_info

def redact_sensitive_info(text, extracted_info):
    for key, value in extracted_info.items():
        text = re.sub(re.escape(value), '[REDACTED]', text)
    return text
