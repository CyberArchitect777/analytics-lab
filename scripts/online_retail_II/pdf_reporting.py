from fpdf import FPDF
import pandas as pd

df = pd.read_csv("../../outputs/csv/online_retail_II_combined.csv", encoding="utf-8")

pdf_report = FPDF()
pdf_report.add_page()
pdf_report.set_font("Helvetica", size=14)

# Parameters: width (0 = full width), height, text, ln (1 to move to next line), align (C=center)
pdf_report.cell(0, 10, "PDF Preview 1 for Online Retail II dataset", ln=True, align="C")
pdf_report.ln(10)
pdf_report.cell(0, 10, "These are shown below:", ln=True, align="C")
pdf_report.ln(10)

pdf_report.set_font("Helvetica", size=12)

# Check how many prices are over 20 in Price column

pdf_report.cell(0, 10, "There are " + str(df[df["Price"] > 10000].shape[0]) + " transactions over 10,000. These are listed below", ln=True, align="L")
pdf_report.ln(10)

page_width = pdf_report.w - pdf_report.l_margin - pdf_report.r_margin

for col in ["Invoice", "StockCode", "Price"]:
    pdf_report.cell(page_width * 0.33, 10, col, border=1, ln=False, align="L")

pdf_report.ln(10)

over_10000 = df[df["Price"] > 10000]

for row in over_10000.iterrows():
    pdf_report.cell(page_width * 0.33, 10, str(row[1]["Invoice"]), border=1, ln=False, align="L")
    pdf_report.cell(page_width * 0.33, 10, str(row[1]["StockCode"]), border=1, ln=False, align="L")
    pdf_report.cell(page_width * 0.33, 10, str(row[1]["Price"]), border=1, ln=True, align="L")

pdf_report.output("../../outputs/pdf/preview1.pdf")