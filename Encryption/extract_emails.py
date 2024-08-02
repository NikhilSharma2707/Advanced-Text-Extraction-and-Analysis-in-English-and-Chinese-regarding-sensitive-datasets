import os
import re


def extract_emails_from_file(file_path):
    """Extract email addresses from a single file."""
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    # Regular expression for extracting email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, file_content)
    return emails


def main():
    # Prompt the user to input the file name or path
    file_path = input("Please enter the file path: ")

    # Extract emails from the specified file
    emails = extract_emails_from_file(file_path)

    # Print the extracted email addresses
    if emails:
        print(f"Emails in {file_path}:")
        for email in emails:
            print(email)
    else:
        print("No emails found or file could not be read.")


if __name__ == "__main__":
    main()
