import re
import os

def extract_emails_from_file(input_filename: str, output_filename: str):
    """
    Automates extracting all email addresses from a source text file and saving unique matches to a destination file.
    """
    print(f"=== Task Automation (Email Extractor) ===")

    if not os.path.exists(input_filename):
        # Create a sample file automatically if it doesn't exist
        sample_text = """
Hello team, please reach out to admin@codealpha.tech or support@ttrpgsim.com for system inquiries. You can also contact developer.joe#python.org directly. invalid emails like test@.com or user@domain should be filtered or handled.
"""
        with open(input_filename, 'w', encoding='utf-8') as f:
            f.write(sample_text)
        print(f"Created sample input file: '{input_filename}'")

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regex pattern for email extraction
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = sorted(list(set(re.findall(email_pattern, content))))

        with open(output_filename, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(email + '\n')

        print(f"Success! Extracted {len(emails)} unique email(s) from '{input_filename}'.")
        print(f"Results saved to '{output_filename}'.")

    except Exception as e:
        print(f"An error occurred during file automation: {e}")

if __name__ == "__main__":
    extract_emails_from_file("Sample_contacts.txt", "extracted_emails.txt")