from pypdf import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import sys
import os
import re
import string
from string import ascii_uppercase
import itertools

# Arg 1 is the Start of Exhibit Range
# Arg 2 is the End of Exhibit Range
# Remember Arg 0 is the call to the scriptfile itself!
start = sys.argv[1]
end = sys.argv[2]
exhibitOrder = []# Array of the exhibit numbers/letters
coverSheets = []# Tuple of (exhibit letter/number,pdf object of cover sheet)

# Generate an array containing the Exhibit numbers/letters
def genRange(start,end):
	global exhibitOrder
	# For letter exhibits
	if not start.isdigit() and not end.isdigit():
		# exhibitOrder = [chr(i) for i in range(ord(start),ord(end)+1)]
		for size in range(len(start),len(end)+1):
			for exhibit in itertools.product(ascii_uppercase, repeat=size):
				exhibitOrder.append(exhibit)
	# For number exhibits
	else:
		exhibitOrder = [i for i in range(int(start),int(end)+1)]

# Create the exhibit cover sheets and hold them in buffer
def genCovers():
	global exhibitOrder
	for exhibit in exhibitOrder:
		sheet = io.BytesIO()
		page = canvas.Canvas(sheet, pagesize=letter)
		page.setFont("Times-Roman", 48)
		text = str("Exhibit %s" % ''.join(exhibit))
		page.drawCentredString(4.25*inch,5.5*inch, text)
		page.save()
		coverSheets.append((exhibit,sheet))

# Save the coversheets as PDFs in CWD
def saveCoversCWD():
	global coverSheets
	for cover in coverSheets:
		exhRaw = ''.join(cover[0])
		padding = '0' if exhRaw.isdigit() else '_'
		width = len(''.join(coverSheets[-1][0]))
		exhForm = f'{exhRaw:{padding}>{width}}'
		output_stream = open("Exhibit_%s_Slipsheet.pdf" % exhForm, "wb")
		output = PdfWriter()
		output.add_page(PdfReader(cover[1]).pages[0])
		output.write(output_stream)
		output_stream.close()

# TODO
# Remove local gen in CWD function
# Replace with function that evaluates a given directory (default: CWD)
# finds PDFs that matches the exhibit from coverSheets(exhibit,sheet)
# Regex to use is something like '/((EXHIBIT|EX.|EXH.|Exhibit|Exh\.+|Ex\.+)[\s-]+[\d\w]*)/'

# function to flush buffer
def cleanSheets():
	return none

genRange(start,end)
genCovers()
saveCoversCWD()

print("Sheets made!")

# Now to write the module where we append the slipsheets to the correct exhibit
# Test edit
#