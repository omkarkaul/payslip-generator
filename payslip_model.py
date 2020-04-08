from fpdf import FPDF

class Payslip:
    def __init__(self, data= dict()):
        self.pdf = FPDF()
        self.data = data
        self.pdf.set_title('payslip')
        self.pdf.set_font('Arial', 'B', 8)
        self.pdf.add_page()

    def write_text(self, x, y, text=""):
        self.pdf.text(20, 20, text)

    def output(self, title):
        self.pdf.output(title, 'F')
