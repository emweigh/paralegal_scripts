# Script that takes in a Relativity data export file + PDF Exports named with the ProdBegBates field, and then:
# (1) recreates the directory structure based on the data export received
# (2) renames the individual documents to their original filenames + bates
# (3) moves renamed copies of individual documents to their original file location per the data export
# Running from CLI: python3 recreate_og_struct.py data.csv

import os
import sys
import csv

def main():
	# Checks that the script when run through the CLI takes in two commands
	# Command 1: is the script itself
	# Command 2: is the CSV file that contains the data we will use
	if len(sys.argv) != 2 and not sys.argv[1].endswith(".csv"):
		print("Usage of script is: python3 %s data.csv\nInput file must be .csv!" % sys.argv[0])
		sys.exit(1)

	# Gets the current working directory which we will need in order to create new directories and move files
	curDir = os.getcwd()

	with open(sys.argv[1], newline='\n') as csvFile:
		exportData = csv.DictReader(csvFile) # creates a DictReader that allows us to access the CSV data by "field"/column name
		
		# Goes through each row and reads the relevant fields
		for row in exportData:
			# Create variables pulling data from the CSV we need to recreate the original folder structure + filenames
			EDFolder = curDir+row['EDFolder'].replace('\\','/')
			fileName = row['Filename'].replace('.pdf','')
			bates = row['ProdBegBates']

			# Assigns the current filename and the new filename (inclusive of file path) to variables to pass
			curFile = "%s\\%s.pdf" % (curDir,bates)
			newFile = "%s\\%s (%s).pdf" % (EDFolder,fileName,bates)

			# Attempts to create the directory
			try:
				os.makedirs(EDFolder)
			except FileExistsError:
				print("Directory '%s' already exists!" % EDFolder)
			else:
				print("Directory '%s' created" % EDFolder)
 			
 			# Attempts to rename the file and move it to the new directory
			try:
				os.rename(curFile,newFile)
			except FileNotFoundError:
				print("\tFile '%s' not found.\n\tNot renamed to '%s (%s).pdf' \n\tNothing moved to %s" % (curFile,fileName,bates,EDFolder))
			else:
				print("\tOriginal file: '%s.pdf' has been renamed to '%s (%s).pdf' and moved to the above directory" % (bates,fileName,bates))
main()