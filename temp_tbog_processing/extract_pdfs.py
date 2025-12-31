import PyPDF2
import sys

def extract_pdf_text(pdf_path, output_path):
    """Extract text from PDF and save to file"""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            
            # Extract text from all pages
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n\n=== PAGE {page_num + 1} ===\n\n"
                text += page.extract_text()
            
            # Save to output file
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            
            print(f"Successfully extracted {len(pdf_reader.pages)} pages from {pdf_path}")
            print(f"Text saved to {output_path}")
            return True
            
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return False

if __name__ == "__main__":
    # Extract Entrega final
    extract_pdf_text(
        "F:/MESGRO/temp_tbog_processing/Entrega final T BOG.pdf",
        "F:/MESGRO/temp_tbog_processing/entrega_final_extracted.txt"
    )
    
    # Extract Memoria
    extract_pdf_text(
        "F:/MESGRO/temp_tbog_processing/Memoria_T BOG.pdf",
        "F:/MESGRO/temp_tbog_processing/memoria_extracted.txt"
    )
