import pdf2image
import pytesseract
import pandas as pd

# PDF file path
pdf_path = "your_document.pdf"

# Convert PDF to images
images = pdf2image.convert_from_path(pdf_path)

# Extract text from each page using OCR
data = []
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang="eng")  # Change lang="hin" for Hindi
    data.append([f"Page {i+1}", text])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Page", "Extracted Text"])

# Save to Excel
excel_path = "extracted_text.xlsx"
df.to_excel(excel_path, index=False)

print(f"OCR Completed! Extracted text saved in '{excel_path}'.")
