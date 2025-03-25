# Takes in an export list
# Evaluates list for any documents that we always produce as Native, i.e. XLSX and XLS (sometimes MP3, MP4, or other audio/video formats)
# Make a dictionary list of Native files with the following attributes: SortDate, DocExt, ProdBegBates
# Now evaluate given Path (Default is CWD) for filenames
# For any filenames in current Path that match ProdBegBates -> rename to following string format "SortDate (YYYY.MM.DD) + NATIVE + (ProdBegBates)"
# Depending on the DocExt, sometimes we replace the "NATIVE" from the above string to other values depending on the Native like "Video" or "Audio"
# But by default we leave spreadsheets as NATIVE

import os
import sys
import csv
import datetime

def main():
	# Checks that the script when run through the CLI takes in two commands
	# Command 1: is the script itself
	# Command 2: is the CSV file that contains the data we will use
	if len(sys.argv) != 2 and not sys.argv[1].endswith(".csv"):
		print("Usage of script is: python3 %s data.csv\nInput file must be .csv!" % sys.argv[0])
		sys.exit(1)

	# Gets the current working directory which we will need in order to create new directories and move files
	curDir = os.getcwd()

	with open(sys.argv[1], newline='\n', encoding='utf-8-sig') as csvFile:
		exportData = csv.DictReader(csvFile) # creates a DictReader that allows us to access the CSV data by "field"/column name
		
		# Goes through each row and reads the relevant fields
		for row in exportData:
			# Check if Group Identifier is empty. If so, then we proceed with processing. Otherwise the document in quesition needs to be handelded by the compile family script
			if row['DocExt'] in ['xlsx','xlsb','xls','mp3','mp4','mkv','wav']:
				# Create variables pulling data from the CSV we need to recreate the original folder structure + filenames
				# Need to rewrite this portion to account for errors if certain fields are blank
				fileName = row['Filename'].rsplit('.',1)[0] if row['Filename'] != '' else 'RENAME'
				docType = row['DocExt']
				bates = row['ProdBegBates']
				date = datetime.datetime.strptime(row['SortDate'],'%m/%d/%Y').strftime('%Y.%m.%d') if row['SortDate'] != '' else 'REDATE'
				
				#Construct newName
				newName = '%s %s NATIVE (%s)' % (date, fileName, bates)

				# Assigns the current filename and the new filename (inclusive of file path) to variables to pass
				curFile = "%s\\%s.%s" % (curDir,bates,docType)
				newFile = "%s\\%s.%s" % (curDir,newName,docType)

				
				# Attempts to rename the file
				try:
					os.rename(curFile,newFile)
				except FileNotFoundError:
					print("\tFile '%s' not found.\n\tNot renamed to '%s (%s).pdf' \n\tNothing renamed" % (curFile,fileName,bates))
				else:
					print("\tOriginal file: '%s.pdf' has been renamed to '%s (%s).pdf' and moved to the above directory" % (bates,fileName,bates))
main()