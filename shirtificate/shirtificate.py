from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(False, margin = 10)

    def header(self):
        self.set_font("helvetica", "B", 40)
        # Printing title "CS50 Shirtificate":
        self.cell(self.epw, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def add_shirt(self):
        self.image("./shirtificate.png", y=70, w=self.epw)

    def add_certificate_text(self, name):
        self.set_font("Times", style="B", size=20)
        self.set_text_color(255,255,255)
        self.ln(90)
        self.cell(self.epw, 20, f"{name} took CS50", align="C")

    def create_shirtificate(self, name):
        self.add_page()
        self.add_shirt()
        self.add_certificate_text(name)

# Instantiation of inherited class
def main():
    name = input("What's your name? ").strip().title()
    pdf = PDF()
    pdf.create_shirtificate(name)
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()