import PyPDF2
import sys
import os

pdf_path = r"F:\MESGRO\temp_meso_processing\Modelación de una simulación de micro corte por SPH en LS-DYNA.pdf"

try:
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += f"\n\n--- PAGE {page_num + 1} ---\n\n"
            text += page.extract_text()
        
        # Save to text file
        output_path = r"F:\MESGRO\temp_meso_processing\pdf_extracted_text.txt"
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        
        print(f"Successfully extracted {len(pdf_reader.pages)} pages")
        print(f"Output saved to: {output_path}")
        print(f"Total characters: {len(text)}")
        
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
