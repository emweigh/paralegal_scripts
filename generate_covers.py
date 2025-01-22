from pypdf import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import sys
import os
import re

# Command 1 is the Start of Exhibit Range
# Command 2 is the End of Exhibit Range
start = sys.argv[1]
end = sys.argv[2]
exhibitOrder = []
coverSheets = []

# Generate an array containing the Exhibit numbers/letters
def genRange():
	global start, end
	global exhibitOrder
	if not start.isdigit() and not end.isdigit():
		exhibitOrder = [chr(i) for i in range(ord(start),ord(end)+1)]
	elif len(end) > 1:
		
	else:
		exhibitOrder = [i for i in range(int(start),int(end)+1)]

# Create the exhibit cover sheets and hold them in buffer
def genCovers():
	global exhibitOrder
	for exhibit in exhibitOrder:
		sheet = io.BytesIO()
		page = canvas.Canvas(sheet, pagesize=letter)
		page.setFont("Times-Roman", 48)
		text = str("Exhibit " + str(exhibit))
		page.drawString(216, 719, text)
		page.save()
		coverSheets.append((exhibit,sheet))

# Save the coversheets as PDFs in CWD
def saveCoversCWD():
	global coverSheets
	for cover in coverSheets:
		output_stream = open("Exhibit " + str(cover[0]) +" Slipsheet.pdf", "wb")
		output = PdfWriter()
		output.add_page(PdfReader(cover[1]).pages[0])
		output.write(output_stream)
		output_stream.close()

genRange()
genCovers()
saveCoversCWD()

# Now to write the portion where we append the slipsheets to the correct exhibit