import fitz  # PyMuPDF
import re
import os
import pickle
from chinese_pattern import extract_chinese_sensitive_info, redact_chinese_sensitive_info
from patterns_in_pdf_recognition import extract_sensitive_info as extract_english_sensitive_info, redact_sensitive_info as redact_english_sensitive_info

# Define the patterns to identify sensitive information in English
patterns = {
    'Full Name': r'Full Name:\s*([^\n]*)',
    'Date of Birth': r'Date of Birth:\s*([^\n]*)',
    'Social Security Number': r'Social Security Number:\s*([^\n]*)',
    'Address': r'Address:\s*([^\n]*)',
    'Phone Number': r'Phone Number:\s*([^\n]*)',
    'Email Address': r'Email Address:\s*([^\n]*)',
    'Bank Name': r'Bank Name:\s*([^\n]*)',
    'Account Number': r'Account Number:\s*([^\n]*)',
    'Routing Number': r'Routing Number:\s*([^\n]*)',
    'Credit Card Number': r'Credit Card Number:\s*([^\n]*)',
    'Expiration Date': r'Expiration Date:\s*([^\n]*)',
    'CVV': r'CVV:\s*([^\n]*)',
    'Health Insurance Provider': r'Health Insurance Provider:\s*([^\n]*)',
    'Policy Number': r'Policy Number:\s*([^\n]*)',
    'Primary Care Physician': r'Primary Care Physician:\s*([^\n]*)',
    'Medical Conditions': r'Medical Conditions:\s*([^\n]*)',
    'Current Medications': r'Current Medications:\s*([^\n]*)',
    'Employer': r'Employer:\s*([^\n]*)',
    'Job Title': r'Job Title:\s*([^\n]*)',
    'Employee ID': r'Employee ID:\s*([^\n]*)',
    'Department': r'Department:\s*([^\n]*)',
    'Work Email': r'Work Email:\s*([^\n]*)',
    'Work Phone': r'Work Phone:\s*([^\n]*)'
}

def load_model():
    model_path = 'C:\\MW\\pythonProject\\data_generation\\PKL File\\model.pkl'
    with open(model_path, 'rb') as file:
        model, vectorizer = pickle.load(file)
    return model, vectorizer

def load_chinese_model():
    model_path = 'C:\\MW\\pythonProject\\data_generation\\PKL File\\Chinese pkl\\model_chinese.pkl'
    with open(model_path, 'rb') as file:
        chinese_model, chinese_vectorizer = pickle.load(file)
    return chinese_model, chinese_vectorizer

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text_blocks = []

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_blocks.extend(page.get_text("blocks"))

    return text_blocks

def predict_sensitive_info(text_blocks, model, vectorizer, patterns):
    sensitive_info = {}
    masked_text = ""

    for block in text_blocks:
        text = block[4]
        original_text = text

        # Vectorize the text for prediction
        text_vect = vectorizer.transform([text])
        prediction = model.predict(text_vect)[0]

        if prediction == 1:
            for key, pattern in patterns.items():
                match = re.search(pattern, original_text)
                if match:
                    sensitive_info[key] = match.group(1)
            # Replace sensitive information in the text with REDACTED
            for key in patterns.keys():
                text = re.sub(patterns[key], f"{key}: REDACTED", text)
        masked_text += text + "\n"

    return sensitive_info, masked_text

def write_text_to_files(sensitive_info, masked_text, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Write sensitive information to a file
    with open(os.path.join(output_dir, "sensitive_info.txt"), "w", encoding='utf-8') as sensitive_file:
        for key, value in sensitive_info.items():
            sensitive_file.write(f"{key}: {value}\n")

    # Write masked text to a file with REDACTED for sensitive information
    with open(os.path.join(output_dir, "files_without_sensitive_info.txt"), "w", encoding='utf-8') as masked_file:
        masked_file.write(masked_text)

def process_pdf(pdf_path, output_folder, model, vectorizer, patterns):
    text_blocks = extract_text_from_pdf(pdf_path)
    sensitive_info, masked_text = predict_sensitive_info(text_blocks, model, vectorizer, patterns)

    write_text_to_files(sensitive_info, masked_text, output_folder)

def process_pdfs(input_folder, output_folder, model, vectorizer, patterns):
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file_name)
            output_subfolder = os.path.join(output_folder, os.path.splitext(file_name)[0])
            process_pdf(pdf_path, output_subfolder, model, vectorizer, patterns)


def process_chinese_pdf(pdf_path, output_folder, model, vectorizer):
    # Open the PDF and extract text
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # Extract sensitive information
    sensitive_info = extract_chinese_sensitive_info(text)

    # Redact sensitive information
    redacted_text = redact_chinese_sensitive_info(text)

    # Save original text with sensitive info
    with open(os.path.join(output_folder, "with_sensitive_info.txt"), 'w', encoding='utf-8') as file:
        file.write(text)

    # Save redacted text
    with open(os.path.join(output_folder, "without_sensitive_info.txt"), 'w', encoding='utf-8') as file:
        file.write(redacted_text)

    # Save PDF with redacted text
    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text("text")
        redacted_page_text = redact_chinese_sensitive_info(page_text)

        # Replace the page text with redacted text
        page.insert_text((72, 72), redacted_page_text, fontsize=11)

    # Save the updated PDF
    doc.save(os.path.join(output_folder, "redacted_output.pdf"))

def process_all_pdfs_chinese(input_folder, output_folder, model, vectorizer):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file_name)
            pdf_output_folder = os.path.join(output_folder, os.path.splitext(file_name)[0])
            if not os.path.exists(pdf_output_folder):
                os.makedirs(pdf_output_folder)
            process_chinese_pdf(pdf_path, pdf_output_folder, model, vectorizer)

def main():
    input_folder_english = "C:\\MW\\pythonProject\\data\\input"
    output_folder_english = "C:\\MW\\pythonProject\\data\\output"
    input_folder_chinese = "C:\\MW\\pythonProject\\data\\chinese_input"
    output_folder_chinese = "C:\\MW\\pythonProject\\data\\output\\chinese_output"

    model, vectorizer = load_model()
    chinese_model, chinese_vectorizer = load_chinese_model()

    process_pdfs(input_folder_english, output_folder_english, model, vectorizer, patterns)
    process_all_pdfs_chinese(input_folder_chinese, output_folder_chinese, chinese_model, chinese_vectorizer)

if __name__ == "__main__":
    main()
