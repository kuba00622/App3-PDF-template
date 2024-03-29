from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, text=row['Topic'],
             align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT,
             border=0)
    pdf.line(10, 21, 200, 21)

    pdf.ln(265)

    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, text=row['Topic'], align="R")

    for a in range(1, 27):
        pdf.set_font(family="Times", style="B", size=8)
        pdf.line(10, 21 + a * 10, 200, 21 + a * 10)


    for i in range(row['Pages']-1):
        pdf.add_page()

        pdf.ln(277)

        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, text=row['Topic'], align="R")

        for a in range(1, 27):
            pdf.set_font(family="Times", style="B", size=8)
            pdf.line(10, 21 + a * 10, 200, 21 + a * 10)



pdf.output("output.pdf")
