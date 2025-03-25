# Compile family pdfs
# Takes in a Relativity export list
# Evaluate list for Group Identifiers
# Create list of families (dicts) that consists of four attributes: Control Number + Family Group Identfier + Filename + ProdBegBates that are associated with Family
# Family Group Identifer = Group Identfier
# Compiled PDF Filename = SortDate (formatted YYYY.MM.DD) + FileName + ProdBegBates
# Note -- list should be sorted so that Bates are in ascending order -- that way when we start compiling they will appear in the right order
# Once done, save a list of FILENAMES from given path (default is CWD)
# Run PDFCreator library to create a new blank PDF
# Then begin iterating through list of families: 1st Family Group ID -> Check List of Bates vs List of FILENAMES -> Every match gets appended to the current PDF
# Once done iterating through list, save current PDF under Compiled PDF Filename
# Need to provide log that also tells while iterating through Bates list for any non-matches

import os
import sys
import csv
import datetime
from pypdf import PdfWriter

def get_familyIDs(family_list : []):
	# identify the family IDs that exist in the current set and returns a list of them
	familyIDs = []
	for member in family_list:
		familyIDs.append(member['GID'])
	familyIDs = sorted(list(dict.fromkeys(familyIDs)))
	return familyIDs
	
def merge_pdfs(pdf_list : [], fileName : str, date : str, master_ext : str):
	merger = PdfWriter()
	for pdf in pdf_list:
		merger.append('%s.pdf' % pdf)
	main_name = fileName.replace('.pdf','') if master_ext not in ['eml','msg'] else 'Email'
	print(pdf_list)
	print(master_ext)
	print("%s %s (%s).pdf" % (date, fileName.replace('.pdf',''), pdf_list[0].replace('.pdf','')))
	merger.write("%s %s (%s).pdf" % (date, main_name, pdf_list[0].replace('.pdf','')))
	for pdf in pdf_list:
		os.remove('%s.pdf' % pdf)
	merger.close()
	
def main():
	# Checks that the script when run through the CLI takes in two commands
	# Command 1: is the script itself
	# Command 2: is the CSV file that contains the data we will use
	if len(sys.argv) != 2 and not sys.argv[1].endswith(".csv"):
		print("Usage of script is: python3 %s data.csv\nInput file must be .csv!" % sys.argv[0])
		sys.exit(1)
		
		
	# Gets the current working directory which we will need in order to create new directories and move files
	curDir = os.getcwd()
	files = [f for f in os.listdir(curDir) if os.path.isfile(f)]

	with open(sys.argv[1], newline='\n', encoding='utf-8-sig') as csvFile:
		exportData = csv.DictReader(csvFile) # creates a DictReader that allows us to access the CSV data by "field"/column name
		#print(exportData.fieldnames)
		member_list =[]
		# Run through export data once -> Get all rows where there is a Group Identiier and create a dict list with attributes: Group ID + Filename + ProdBegBates
		# Need to also determine the starting doc in compilation -> This is where Control Number = Group Identifier
		
		for row in exportData:
			# Check if Group Identifier has a value assigned. If so, then prepare a dict and then add to list of family members
			write_filename = lambda a, b, c: os.path.splitext(b)[0] if a == c else ''
			
			if row['Group Identifier'] != '':
				member = {\
					'GID' : row['Group Identifier'],
					'Control' : row['Control Number'],\
					'Filename' : write_filename(row['Control Number'], row['Filename'], row['Group Identifier']),
					'Ext' : row['DocExt'],\
					'Bates' : row['ProdBegBates'],\
					'Date' : datetime.datetime.strptime(row['SortDate'],'%m/%d/%Y').strftime('%Y.%m.%d')}
				member_list.append(member)
		print(member_list)
		family_list = get_familyIDs(member_list)
		print(family_list)
		for family in family_list:
			merge_list= []
			for member in member_list:
				if family == member['GID']:
					merge_list.append("%s" % member['Bates'])
			merge_list.sort()
			#assign_member_value = lambda a,b,c: next((member[a] for member in member_list if member[b] == c, '')
			to_name = next((member['Filename'] for member in member_list if member["Bates"] == merge_list[0]), '')
			to_date = next((member['Date'] for member in member_list if member["Bates"] == merge_list[0]), '')
			to_ext = next((member['Ext'] for member in member_list if member["Bates"] == merge_list[0]), '')
			merge_pdfs(merge_list, to_name, to_date, to_ext)
main()