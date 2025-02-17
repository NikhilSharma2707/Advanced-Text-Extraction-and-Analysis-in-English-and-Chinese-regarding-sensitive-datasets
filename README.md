# Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets

This sophisticated application automates the masking of sensitive information within PDF documents, catering to both English and Chinese text.
Leveraging machine learning and regex-based pattern recognition, it efficiently redacts personal details while maintaining the original document layout. 
Designed for versatility, it is suitable for both small-scale and enterprise-level data protection, ensuring comprehensive privacy and security.
Advanced Data Extraction and Machine Learning Analytics on Distinct English and Chinese Datasets ### Project Overview This advanced application automates the masking of sensitive information in PDF documents. 

- It supports both English and Chinese text
- utilizing machine learning and regex-based pattern recognition to redact personal details while preserving the original layout.
- This tool is ideal for both small-scale and enterprise data protection. 

## Features
- #### Supports English and Chinese PDFs**: Handles sensitive data in both languages.
- #### Regex and Machine Learning**: Uses a combination of regex patterns and machine learning models for accurate information extraction and redaction. -
- #### Preserves Original Layout: Ensures the output PDF maintains the same layout and structure as the original.
- #### Generates Redacted and Non-Redacted Text Files**: Provides both versions for verification and compliance purposes.
                
### Prerequisites Before you begin, ensure you have met the following requirements: 
- Python 3.8+
-  Git - Required Python packages (listed in `requirements.txt`) 

### Installation
1. ### Clone the Repository:
      ```bash
   git clone https://github.com/brucewayneoptimusprime/Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets.git cd Advanced-Data-Extraction-and-Machine-Learning-Analytics-on-Distinct-English-and-Chinese-Datasets

2. ### Create a Virtual Environment:
   ```bash
    python -m venv .venv

4. ### Activate the Virtual Environment :
    - On Windows: ```bash
      .venv\Scripts\activate```
    - On macOS and Linux: ```bash
       source .venv/bin/activate```
5. ### Install Required Packages:
    ```bash
   pip install -r requirements.txt ``` 

7. ### Place Your PDFs:
   - For English PDFs, place them in the `data/input` directory.
   - For Chinese PDFs, place them in the `data/chinese_input` directory.
8. ### Execute the Main Script:
    ```bash
   python main.py ```


### Output
The redacted PDFs will be saved in `data/output` and `data/output/chinese_output` respectively. 
- Text files with and without sensitive information will also be generated in the respective output directories. 


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

  
To run the Flask application, follow these steps:

1. **Install Flask**:
   Ensure you have Flask installed. You can install it using pip:

   ```bash
   pip install Flask

2. **TO RUN THE FILE**:
   Use the following command in your terminal or command prompt to start the Flask application:

   ```bash
   python app.py

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
`````

## `qr_code_generator.py`
This script generates multiple QR codes with unique static keys derived from file names and saves them in a specified folder. The static keys are associated with different files.

### Functions

- Generates a static key by hashing the file name with SHA-256.
- Returns the hashed key.
-Creates a QR code containing the provided data and saves the QR code image to the specified file path.

### Detailed Description
The script creates a static key for each file by hashing its name.
It then generates a QR code that encodes this static key and the file name.

The QR codes are saved in the specified folder, with each QR code associated with a different file.

When scanned, each QR code reveals the static key associated with a different file.

#### 1. **Update the PDF Path**:
   - Modify the path variable in the script to point to your folders where sensitive info is stored
     
#### 2. **Run the Script**:
   ```bash
   python qr_code_generator.py
`````

## `send_mail.py(Future Application)`
This script sends an email with a QR code attachment to a specified recipient using the Mailjet API. The email subject includes randomly generated info.
### Functions
Sends an email with the QR code attachment using the Mailjet API to the user whose sensitive information file is present. The email is extracted from the `extract_emails.py` file. This is not fully functional yet it is for future application.

#### 2. **Run the Script**:
   ```bash
   python send_email_with_qr.py
`````

## Authors
- [**Nikhil Sharma**](https://github.com/NikhilSharma2707)
- [**Aditya Vikram Singh**](https://github.com/brucewayneoptimusprime)
- [**Aditya Teotia**](https://github.com/Adityaa050)




