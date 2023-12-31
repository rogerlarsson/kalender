from fpdf import FPDF
import datetime

def kalender(year = 2024, weeks = range(1, 53), filename = "kalender.pdf", rowsperday = 18):
    wds = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    pdf = FPDF(orientation = "L", unit = "mm", format = "A4")
    pdf.set_font("helvetica", "I", 12)
    for w in weeks:
        pdf.add_page()
        with pdf.table() as table:
            row = table.row()
            for d, wd in enumerate(wds, start = 1):
                v = f"Vecka {w}" if d == 1 else " "
                dt = datetime.date.fromisocalendar(year, week = w, day = d)
                row.cell(text = f"{v}\n{wd}\n{dt}")
            for r in range(rowsperday):
                row = table.row()
                for wd in wds:
                    row.cell(f" ")
                    #row.cell(f"vecka {w} rad {r}")
    pdf.output(filename)

kalender()
