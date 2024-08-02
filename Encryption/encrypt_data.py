# encrypt_data.py

from extract_text import extract_text_from_pdf
from aes_cipher import AESCipher
from qr_code_generator import generate_random_key, create_qr_code


def main(pdf_path, encrypted_file_path, qr_code_path):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Generate random key and create QR code
    random_key = generate_random_key()
    create_qr_code(random_key, qr_code_path)

    # Encrypt text
    cipher = AESCipher(random_key)
    encrypted_text = cipher.encrypt(text)

    # Save encrypted text to file
    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted_text)


# Example usage
if __name__ == '__main__':
    pdf_path = "sensitive_info.pdf"
    encrypted_file_path = "encrypted_data.txt"
    qr_code_path = "random_key_qr.png"

    main(pdf_path, encrypted_file_path, qr_code_path)
