import pandas as pd
from fpdf import FPDF

# Excel file load karo
df = pd.read_excel("sample_invoice_data.xlsx")

# Har row ka alag PDF invoice banao
for index, row in df.iterrows():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Invoice", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Invoice No: {row['Invoice No']}", ln=True)
    pdf.cell(200, 10, txt=f"Customer Name: {row['Name']}", ln=True)
    pdf.cell(200, 10, txt=f"Product: {row['Product']}", ln=True)
    pdf.cell(200, 10, txt=f"Quantity: {row['Quantity']}", ln=True)
    pdf.cell(200, 10, txt=f"Price: Rs. {row['Price']}", ln=True)
    pdf.cell(200, 10, txt=f"Total: Rs. {row['Total']}", ln=True)

    # File name with invoice number
    file_name = f"invoice_{row['Invoice No']}.pdf"
    pdf.output(file_name)
    print(f"Invoice generated: {file_name}")
