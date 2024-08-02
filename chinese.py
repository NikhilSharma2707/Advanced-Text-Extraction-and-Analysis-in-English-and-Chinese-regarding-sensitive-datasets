import fitz  # PyMuPDF
import os
import pickle
from chinese_pattern import extract_chinese_sensitive_info, redact_chinese_sensitive_info

def load_chinese_model():
    with open("C:\\MW\\pythonProject\\data_generation\\PKL File\\Chinese pkl\\model_chinese.pkl", 'rb') as file:
        model, vectorizer = pickle.load(file)
    return model, vectorizer

def process_chinese_pdf(pdf_path, output_folder, model, vectorizer):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    sensitive_info = extract_chinese_sensitive_info(text)
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
        page_text = redact_chinese_sensitive_info(page_text)
        page.insert_text((72, 72), page_text, fontsize=11)

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

if __name__ == "__main__":
    input_folder = "C:\\MW\\pythonProject\\data\\chinese_input"
    output_folder = "C:\\MW\\pythonProject\\output_pdfs\\chinese"
    model, vectorizer = load_chinese_model()
    process_all_pdfs_chinese(input_folder, output_folder, model, vectorizer)
