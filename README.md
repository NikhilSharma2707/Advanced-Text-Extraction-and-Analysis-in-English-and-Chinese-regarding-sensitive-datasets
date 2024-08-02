**Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets**

This sophisticated application automates the masking of sensitive information within PDF documents, catering to both English and Chinese text. 
Leveraging machine learning and regex-based pattern recognition, it efficiently redacts personal details while maintaining the original document layout. 
Designed for versatility, it is suitable for both small-scale and enterprise-level data protection, ensuring comprehensive privacy and security.

Advanced Data Extraction and Machine Learning Analytics on Distinct English and Chinese Datasets
Project Overview
This advanced application automates the masking of sensitive information in PDF documents. It supports both English and Chinese text, utilizing machine learning and regex-based pattern recognition to redact personal details while preserving the original layout. This tool is ideal for both small-scale and enterprise data protection.

Features
Supports English and Chinese PDFs: Handles sensitive data in both languages.
Regex and Machine Learning: Uses a combination of regex patterns and machine learning models for accurate information extraction and redaction.
Preserves Original Layout: Ensures the output PDF maintains the same layout and structure as the original.
Generates Redacted and Non-Redacted Text Files: Provides both versions for verification and compliance purposes.
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.8+
Git
Required Python packages (listed in requirements.txt)
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/brucewayneoptimusprime/Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets.git
cd Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets
Create a Virtual Environment

bash
Copy code
python -m venv .venv
Activate the Virtual Environment

On Windows:
bash
Copy code
.venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source .venv/bin/activate
Install Required Packages

bash
Copy code
pip install -r requirements.txt
Usage
Running the Tool
Place Your PDFs

For English PDFs, place them in the data/input directory.
For Chinese PDFs, place them in the data/chinese_input directory.
Execute the Main Script

bash
Copy code
python main.py
Output
The redacted PDFs will be saved in data/output and data/output/chinese_output respectively.
Text files with and without sensitive information will also be generated in the respective output directories.
File Structure
graphql
Copy code
Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets/
│
├── data/
│   ├── input/                   # English PDFs
│   ├── output/                  # Output directory for English PDFs
│   │   ├── redacted_output.pdf  # Redacted English PDF
│   │   ├── with_sensitive_info.txt
│   │   └── without_sensitive_info.txt
│   ├── chinese_input/           # Chinese PDFs
│   └── output/chinese_output/   # Output directory for Chinese PDFs
│       ├── redacted_output.pdf  # Redacted Chinese PDF
│       ├── with_sensitive_info.txt
│       └── without_sensitive_info.txt
│
├── pythonProject/
│   ├── main.py                  # Main script
│   ├── chinese_pattern.py       # Chinese text extraction and redaction
│   └── other scripts...         # Additional scripts for functionality
│
├── requirements.txt             # Python packages required
└── README.md                    # Project readme
Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or issues, please contact Aditya Vikram Singh.

# Encryption Folder

This folder contains the code and resources related to the encryption functionality of the project. Below is an overview of the folder's structure and its contents:

## `__pycache__` Directory

The `__pycache__` directory contains compiled Python files, which are automatically generated when the Python scripts are run. The compiled files in this directory correspond to the following Python scripts:

- `aes_cipher.py` - Contains functionality for AES encryption and decryption.
- `extract_text.py` - Handles text extraction from sensitive datasets.
- `qr_code_generator.py` - Generates QR codes for secure access.

## `templates` Directory

The `templates` directory contains HTML files used by the Flask application to provide user interfaces for key verification.

### `index.html`

This is the main HTML form where users can enter their generated key to gain access to sensitive data.

### `error.html`

The HTML page displayed when an incorrect key is entered. It notifies the user of the error and provides a link to retry

## `app.py`

The Flask application file that provides the user interface and handles key verification. It contains the following routes:


### Key Components
##### KEY_FILE_URLS Dictionary: 
Maps valid keys to their respective Google Drive file URLs. This dictionary is used to determine which file URL to redirect to based on the entered key.

##### Flask Routes:

- index() - Renders the index.html template.

- verify_key() - Verifies the provided key and redirects to the appropriate file URL or shows an error page.

- download_file() - Redirects to the file URL (can be utilized for additional functionality related to file downloads)

## `aes_cipher.py`
This file implements the AES encryption and decryption functionality using the pycryptodome library. It defines the AESCipher class with methods to encrypt and decrypt text.

### Key Features
- Encrypt - Encrypts plaintext using a provided key.
- Decrypt - Decrypts the encrypted text using the same key.
- Padding - Handles padding to ensure that plaintext length is a multiple of the block size.

## `extract_text_from_pdf.py`

The extract_text_from_pdf.py file provides functionality for extracting text from PDF files. It uses the PyPDF2 library to read and extract text content from each page of a PDF. The file contains the following functionality:

### Functionalities
- Text Extraction from PDF:

Purpose: Extracts all text from a specified PDF file.

Description: Opens the provided PDF file, reads its content, and extracts text from each page. The extracted text is concatenated into a single string and returned.
- Error Handling:

File Not Found: Handles the case where the specified PDF file does not exist, and prints an appropriate error message.

General Exceptions: Catches and prints any other exceptions that may occur during the file reading and text extraction process.

To extract text from a PDF file using the script, follow these steps:

#### 1. **Update the PDF Path**:
   - Modify the `pdf_path` variable in the script to point to your PDF file.

#### 2. **Run the Script**:
   - Use the following command in your terminal or command prompt:

   ```bash
   python extract_text_from_pdf.py
