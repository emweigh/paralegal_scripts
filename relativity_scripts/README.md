## relativity_scripts

### *recreate_og_struct.py*
>This script recreates the EDFolder structure of exports and moves individual documents to their original EDFolder location

### *rename&compile_family_export.py*
>This script parses a .CSV export file, identifies family groups, and then compiles individual family members into a single .PDF. Built in filename format is "YYYY.MM.DD FileName Bates"

### *rename_native_export.py*
>IDs non-PDF document exports and renames them to following filename format: "YYYY.MM.DD FileName Bates NATIVE"

### *rename_singleton_export.py*
>This script parses a .CSV export file, identifies documents that are not part of family groups, and then renames to the following filename format: "YYYY.MM.DD FileName Bates"
