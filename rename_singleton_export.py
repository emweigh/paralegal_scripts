# Script that takes in a Relativity data export file + PDF Exports named with the ProdBegBates field, and then:
# (1) recreates the directory structure based on the data export received
# (2) renames the individual documents to their original filenames + bates
# (3) moves renamed copies of individual documents to their original file location per the data export
# Running from CLI: python3 recreate_og_struct.py data.csv

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
			if row['Group Identifier'] == '':
				# Create variables pulling data from the CSV we need to recreate the original folder structure + filenames
				# Need to rewrite this portion to account for errors if certain fields are blank
				fileName = row['Filename'].replace('pdf','') if row['Filename'] != '' else 'RENAME'
				docType = row['DocExt']
				bates = row['ProdBegBates']
				date = datetime.datetime.strptime(row['SortDate'],'%m/%d/%Y').strftime('%Y.%m.%d') if row['SortDate'] != '' else 'REDATE'
				
				#Construct newName
				newName = '%s %s (%s)' % (date, 'Email' if docType in ['msg', 'eml'] else fileName, bates)

				# Assigns the current filename and the new filename (inclusive of file path) to variables to pass
				curFile = "%s\\%s.pdf" % (curDir,bates)
				newFile = "%s\\%s.pdf" % (curDir,newName)

				
				# Attempts to rename the file
				try:
					os.rename(curFile,newFile)
				except FileNotFoundError:
					print("\tFile '%s' not found.\n\tNot renamed to '%s (%s).pdf' \n\tNothing renamed" % (curFile,fileName,bates))
				else:
					print("\tOriginal file: '%s.pdf' has been renamed to '%s (%s).pdf' and moved to the above directory" % (bates,fileName,bates))
main()