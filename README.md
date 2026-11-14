# CodeAlpha_Automation

An automated email extraction script built in Python as part of the CodeAlpha Python Programming Internship.

---

## 🚀 Features
- **Automated Sample Generation**: Automatically creates a sample contact file if none exists, ensuring zero-configuration startup.
- **Regular Expression Parsing**: Uses precise regex patterns to scan raw text files and isolate valid email addresses.
- **Unique Sorting & Export**: Deduplicates and sorts extracted email addresses before writing them to a clean output text file.

## 🛠️ Key Concepts Used
- Regular expressions (`re` module)
- File handling and exception management (`os` module)
- Set deduplication and string sorting

## 📂 Project Structure
```text
CodeAlpha_Automation/
├── automation.py
├── Sample_contacts.txt (Auto-generated if missing)
├── extracted_emails.txt
└── README.md
