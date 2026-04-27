import fitz

pdf_path = "Number Sense/number sense tricks manual.pdf"  # Replace with your PDF file path
output_path = "Number Sense/output.txt"  # Replace with your desired output file path


doc = fitz.open(pdf_path)
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    
    with open(output_path, "a") as f:
        f.write(text)

print(f"Text extracted and saved to {output_path}")