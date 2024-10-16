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
