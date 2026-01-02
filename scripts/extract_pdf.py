
from pypdf import PdfReader
import sys

def extract_text(pdf_path, output_txt):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully extracted text to {output_txt}")
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_text(r"f:\MESGRO\assets\schematics\ebarisbot\report.pdf", r"f:\MESGRO\scripts\report_content.txt")
