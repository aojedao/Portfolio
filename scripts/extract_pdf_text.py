#!/usr/bin/env python3
import PyPDF2
import os

pdf_files = {
    "Final Project": r"H:\My Drive\Advanced Mechatronics\Final Project\Final Project Report.pdf",
    "1st Mini Project": r"H:\My Drive\Advanced Mechatronics\1st Mini Project\Project 1 Report.pdf",
    "2nd Mini Project": r"H:\My Drive\Advanced Mechatronics\2nd Mini Project\Project 2 Report.pdf"
}

for project_name, pdf_path in pdf_files.items():
    if not os.path.exists(pdf_path):
        # Try alternative names
        base_dir = os.path.dirname(pdf_path)
        base_name = project_name.lower().replace(" ", "_")
        
        # Look for any PDF in the directory
        if os.path.exists(base_dir):
            pdfs = [f for f in os.listdir(base_dir) if f.lower().endswith('.pdf')]
            if pdfs:
                pdf_path = os.path.join(base_dir, pdfs[0])
    
    if os.path.exists(pdf_path):
        print(f"\n{'='*60}")
        print(f"{project_name}")
        print(f"{'='*60}")
        
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                print(f"Total pages: {len(reader.pages)}\n")
                
                # Extract first 2 pages
                for i in range(min(2, len(reader.pages))):
                    text = reader.pages[i].extract_text()
                    print(f"--- Page {i+1} ---")
                    print(text[:700])
                    print()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"\n❌ Not found: {pdf_path}")
