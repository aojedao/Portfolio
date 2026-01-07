import pdfplumber
from pathlib import Path

pdf_files = [
    r"C:\Users\USER\Documents\NYU\FOR\P2\ojeda_alejandro_P2.pdf",
    r"C:\Users\USER\Documents\NYU\FOR\P3\ojeda_alejandro_P3.pdf"
]

for pdf_path in pdf_files:
    print(f"\n{'='*80}")
    print(f"EXTRACTING: {pdf_path}")
    print(f"{'='*80}\n")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Total Pages: {len(pdf.pages)}\n")
            
            all_text = []
            
            for i, page in enumerate(pdf.pages, 1):
                print(f"--- PAGE {i} ---")
                text = page.extract_text()
                if text:
                    all_text.append(text)
                    print(text)
                    print()
                
                # Also try to extract tables if they exist
                tables = page.extract_tables()
                if tables:
                    print(f"[TABLES DETECTED ON PAGE {i}]")
                    for j, table in enumerate(tables, 1):
                        print(f"Table {j}:")
                        for row in table:
                            print(row)
                    print()
            
            print(f"\n{'='*80}")
            print(f"END OF DOCUMENT: {Path(pdf_path).name}")
            print(f"{'='*80}\n")
            
    except Exception as e:
        print(f"ERROR processing {pdf_path}: {e}\n")
