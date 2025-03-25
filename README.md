# To Do List

## generate_covers

- [X] ~~Add function that will allow exhibits ranges starting from AA - ZZ~~
- [ ] Add function that will match exhibit PDFs with corresponding coversheet PDF
- [ ] Add function that will merge coversheet with exhibit PDFs
- [ ] Rewrite cover sheet gen function to select directory to save or create new function to do that

## relativity_scripts
- [ ] Rewrite argument handling to use argparse modules for better argument handling and also to create an easier "help" interface for users


# Summary of Scripts

## generate_covers

#### *generate_covers.py*
<table><tr><td>This script allows you to generate cover sheets for exhibits - both letter and number exhibits!</td></tr></table>

## relativity_scripts

#### *recreate_og_struct.py*
<table><tr><td>This script recreates the EDFolder structure of exports and moves individual documents to their original EDFolder location</td></tr></table>

#### *rename&compile_family_export.py*
<table><tr><td>This script parses a .CSV export file, identifies family groups, and then compiles individual family members into a single .PDF. Built in filename format is "YYYY.MM.DD FileName Bates"</td></tr></table>

#### *rename_native_export.py*
<table><tr><td>IDs non-PDF document exports and renames them to following filename format: "YYYY.MM.DD FileName Bates NATIVE"</td></tr></table>

#### *rename_singleton_export.py*
<table><tr><td>This script parses a .CSV export file, identifies documents that are not part of family groups, and then renames to the following filename format: "YYYY.MM.DD FileName Bates"</td></tr></table>
