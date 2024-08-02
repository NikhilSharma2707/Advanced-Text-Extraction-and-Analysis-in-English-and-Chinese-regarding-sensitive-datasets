import os
import secrets
import segno

def generate_random_key():
    return secrets.token_urlsafe(16)

def create_qr_code(data, file_path, scale=20):
    qr = segno.make(data)
    qr.save(file_path, scale=scale)

if __name__ == "__main__":
    random_key = generate_random_key()
    print(f"Generated key: {random_key}")

    # Define the directory where you want to save the QR code image
    folder_path = "C:\\MW\\QR"

    # Ensure the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the complete file path
    file_name = "qr_code.png"
    file_path = os.path.join(folder_path, file_name)

    # Create and save the QR code with the verification URL
    url = f"http://localhost:5000/verify_key?key={random_key}"
    create_qr_code(url, file_path, scale=20)
    print(f"QR code saved to {file_path}")
