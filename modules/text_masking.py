def mask_sensitive_info(text, clinic_names):
    # Example masking function with debug prints
    print(f'Original Text: {text}')
    # Apply masking logic (dummy example here)
    sensitive_info = {
        "Full Name": "[REDACTED]",
        "Date of Birth": "[REDACTED]",
        "Social Security Number": "[REDACTED]",
        "Address": "[REDACTED]",
        "Phone Number": "[REDACTED]",
        "Email Address": "[REDACTED]",
        "Bank Name": "[REDACTED]",
        "Account Number": "[REDACTED]",
        "Routing Number": "[REDACTED]",
        "Credit Card Number": "[REDACTED]",
        "Expiration Date": "[REDACTED]",
        "CVV": "[REDACTED]",
        "Health Insurance Provider": "[REDACTED]",
        "Policy Number": "[REDACTED]",
        "Primary Care Physician": "[REDACTED]",
        "Medical Conditions": "[REDACTED]",
        "Current Medications": "[REDACTED]",
        "Employer": "[REDACTED]",
        "Job Title": "[REDACTED]",
        "Employee ID": "[REDACTED]",
        "Department": "[REDACTED]",
        "Work Email": "[REDACTED]",
        "Work Phone": "[REDACTED]"
    }

    for key, value in sensitive_info.items():
        if key in text:
            text = text.replace(key, f'{key}: {value}')

    print(f'Masked Text: {text}')
    return text
