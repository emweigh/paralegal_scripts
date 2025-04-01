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
				exhibitOrder.append(''.join(exhibit))
	# For number exhibits
	else:
		exhibitOrder = [i for i in range(int(start),int(end)+1)]

# Create the exhibit cover sheets and hold them in buffer
def genCovers():
	global exhibitOrder
	# Going through array of exhibit numbers
	for exhibit in exhibitOrder:
		# Generate a blank PDF sheet
		sheet = io.BytesIO()
		page = canvas.Canvas(sheet, pagesize=letter)
		
		# Setting properties of PDF
		page.setFont("Times-Bold", 48)
		text = str("EXHIBIT %s" % ''.join(str(exhibit)))
		
		# Write Exhibit Text to PDF page
		page.drawCentredString(4.25*inch,5.5*inch, text)
		page.save()
		
		# Save current exhibit cover sheet to array
		# Sheet is saved as a tuple where (str: Exhibit Number, pdf: Exhibit Sheet PDF)
		coverSheets.append((exhibit,sheet))

# Save the coversheets as PDFs in CWD
def saveCoversCWD():
	global coverSheets
	
	# Going through array of saved PDF cover sheets
	for cover in coverSheets:
		# We call for the raw exhibit number because we might need to add 'padding' to it later
		exhRaw = ''.join(str(cover[0]))
		
		# Check if our 'numbering' is digits or letters, and set our padding to the appropriate character: '0' or '_'
		padding = '0' if exhRaw.isdigit() else '_'
		
		# Check the last exhibit number. This determines how much padding we need
		# e.g. if the last exhibit is 100, then that means we need to pad up to 3 digits, so Exhibit 1 => Exhibit 001
		width = len(''.join(str(coverSheets[-1][0])))
		
		# f-string padding here
		# Still confused a bit on how this works but
		# We've already taken the raw exhibit number
		# Now we call it in a f-string but also call for some formatting
		# We already set 'padding' and 'width' previously
		# Now we call exhRaw in the f-string and pass three values to format it
		# The values are: '{padding', '>', and '{width}'.
		# '{}' around the previously defined values to call them in an f-string
		# The '>' indicates that the padding will go on the left end of whatever string/sub-string is being formatted
		# You can also use '^' or '<' to indicate padding that is centered or right aligned
		# Seems that calling formatting like this is position based so you need to pass in the order as shown here
		# NOTE: 'padding' variable only seems to be accepted if it's a single character string.
		exhForm = f'{exhRaw:{padding}>{width}}'
		
		# Open a new file and name it
		output_stream = open("Exhibit_%s_Slipsheet.pdf" % exhForm, "wb")
		
		# Instantiate a PDFWriter class which effectively says create a PDF
		output = PdfWriter()
		
		# Add pages to the writer
		# Forget why we need to call PdfReader on this if we already 
		# generated PDFs that are being held in coverSheets
		# Check: can we add to output without calling PdfReader?
		output.add_page(PdfReader(cover[1]).pages[0])
		
		# Write the current PDF to the new file
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