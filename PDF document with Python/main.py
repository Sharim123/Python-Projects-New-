from fpdf import FPDF

pdf = FPDF(orientation="P", unit='pt', format='A4')
pdf.add_page()

pdf.image('fpic.png', w=80, h=50)

pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0, h=50, txt="Sun Flower", align='C', ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=15, txt="Description", ln=1)

pdf.set_font(family="Times", size=12)
txt1 = "The common sunflower (Helianthus annuus) is a large annual forb of the genus Helianthus. It is commonly grown as a crop for its edible oily seeds. Apart from cooking oil production, it is also used as livestock forage (as a meal or a silage plant), as bird food, in some industrial applications, and as an ornamental in domestic gardens. Wild H. annuus is a widely branched annual plant with many flower heads. The domestic sunflower, however, often possesses only a single large inflorescence (flower head) atop an unbranched stem."
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Kingdom:")

pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=25, txt="Animalia", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Phylum:")

pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=25, txt="Chordata", ln=1)

pdf.output('output.pdf')