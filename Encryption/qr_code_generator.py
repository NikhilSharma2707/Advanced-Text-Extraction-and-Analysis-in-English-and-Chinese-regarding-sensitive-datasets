import os
import segno
import hashlib

def generate_static_key(file_name):
    # Create a static key by hashing the file name
    return hashlib.sha256(file_name.encode()).hexdigest()

def create_qr_code(data, file_path, scale=20):
    qr = segno.make(data)
    qr.save(file_path, scale=scale)

if __name__ == "__main__":
    num_qr_codes = 10  # Number of QR codes to generate
    folder_path = r"C:\MW\QR"  # Ensure the path is raw string to handle backslashes
    sample_dir = r"C:\MW\sample testing"  # Directory with sensitive info files

    # Ensure the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Get the list of files in the sample directory
    files = os.listdir(sample_dir)
    if len(files) < num_qr_codes:
        print(f"Not enough files in the directory {sample_dir}")
        num_qr_codes = len(files)

    for i in range(num_qr_codes):
        file_name = files[i]
        file_path = os.path.join(folder_path, f"qr_code_{i + 1}.png")

        # Generate a static key based on the file name
        static_key = generate_static_key(file_name)

        # The data to be encoded in the QR code
        data = f"Key: {static_key}\nFile: {file_name}"

        # Create and save the QR code
        create_qr_code(data, file_path, scale=20)
        print(f"QR code {i + 1} saved to {file_path} with key {static_key} associated to file {file_name}")
