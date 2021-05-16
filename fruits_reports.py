#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

desc_loc = "./supplier-data/descriptions"

def generate_summary():
  summary = []
  for file in os.listdir(desc_loc):
    d_filename = os.path.join(desc_loc, file)
    with open(d_filename, 'r') as f:
      name = f.readline().strip()
      weight = f.readline().strip()
      description = f.readline().strip()
      summary.append("<br/>name: {}\nweight: {}<br/>".format(name, weight))
  return summary
    
def generate_report(filename):
  summary = "\n\n".join(generate_summary())
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph("Processed Update on {}".format(datetime.today().strftime('%B %d, %Y')), styles["h1"])
  report_info = Paragraph(summary, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])

if __name__ == "__main__":
  generate_report("/tmp/processed.pdf")