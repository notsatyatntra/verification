import pandas as pd
from fpdf import FPDF
import os

# Define paths
csv_output_dir = "csv_files"
pdf_output_dir = "pdf_files_new"
os.makedirs(pdf_output_dir, exist_ok=True)

def generate_pdf_from_csv(csv_filepath, pdf_filepath):
    # Load CSV file
    data = pd.read_csv(csv_filepath)
    
    # Create a PDF document
    data['Content'] = data['Content'].fillna('')

    # Extract the Title and Text columns
    titles = data['Name']
    texts = data['Content']

    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content to PDF
    for title, text in zip(titles, texts):
        pdf.set_font("Arial", style='B', size=14)  # Bold for title
        pdf.cell(0, 10, title.encode('latin1', 'replace').decode('latin1'), ln=True)
        pdf.set_font("Arial", size=12)  # Normal for text
        pdf.multi_cell(0, 10, text.encode('latin1', 'replace').decode('latin1'))
        pdf.ln(10)  # Add a line break between entries

    # Save the PDF
    pdf.output(pdf_filepath)
    print(f"PDF saved to {pdf_filepath}")

csv_files = [f for f in os.listdir(csv_output_dir) if f.endswith('.csv')]

for idx, csv_file in enumerate(csv_files):
    csv_filepath = os.path.join(csv_output_dir, csv_file)
    pdf_filename = f"website_{idx+1}.pdf"
    pdf_filepath = os.path.join(pdf_output_dir, pdf_filename)
    generate_pdf_from_csv(csv_filepath, pdf_filepath)
    break

print("All PDFs generated successfully.")
