# TODO:

## generate_covers.py

1. ~~Add function that will allow exhibits ranges starting from AA - ZZ~~
2. Add function that will match exhibit PDFs with corresponding coversheet PDF
3. Add function that will merge coversheet with exhibit PDFs
4. Rewrite cover sheet gen function to select directory to save or create new function to do that
  
# Summary of Scripts
The scripts contained in this repository are designed to take in a document export from Relativity and a .CSV export of associated fields in order to perform PDF batch operations.

## recreate_og_struct.py
This script recreates the EDFolder structure of exports and moves individual documents to their original EDFolder location

## rename&compile_family_export.py
This script parses a .CSV export file, identifies family groups, and then compiles individual family members into a single .PDF. Built in filename format is "YYYY.MM.DD FileName Bates"

## rename_native_export.py
IDs non-PDF document exports and renames them to following filename format: "YYYY.MM.DD FileName Bates NATIVE"

## rename_singleton_export.py
This script parses a .CSV export file, identifies documents that are not part of family groups, and then renames to the following filename format: "YYYY.MM.DD FileName Bates"
>>>>>>> fe5ac9c322817ae997bb32055eb140350fcc2f9b
