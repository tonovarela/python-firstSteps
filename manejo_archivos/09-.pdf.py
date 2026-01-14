from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Hola, este es un archivo PDF generado con FPDF en Python.", ln=True, align='C')
pdf.cell(200, 10, txt="PDF generado por python", ln=True, align='C')
pdf.output("archivo_generado.pdf")