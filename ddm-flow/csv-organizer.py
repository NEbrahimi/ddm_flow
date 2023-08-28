#This script makes copies of the CSV files generated in using create-csv-for-pcd-analysis-folder.py and places them in
# relevant sub-folders.It establishes a directory titled "analysis-individual-filter" and constructs any necessary
# sub-directories to sort CSV files based on specific filters.

import os
import shutil
import pandas as pd
import re

parent_dir = 'C:/Users/z3541106/unsw/analysis/pcd-modulation-megan'

# Ensure "analysis-individual" folder exists
analysis_dir = os.path.join(parent_dir, 'analysis-individual-filter')
if not os.path.exists(analysis_dir):
    os.makedirs(analysis_dir)

# Iterate over all subdirectories in the parent directory
for subdir, dirs, files in os.walk(parent_dir):
    if "OutputsDDM" in dirs:
        ddm_dir = os.path.join(subdir, "OutputsDDM")
        for file in os.listdir(ddm_dir):
            if file.endswith(".csv"):
                file_path = os.path.join(ddm_dir, file)

                # Extract the 'F' number from the filename using regex
                match = re.search(r'F(\d+)', file)
                if not match:
                    continue

                F_number = 'F' + match.group(1)

                # Ensure F folder exists
                F_folder = os.path.join(analysis_dir, F_number)
                if not os.path.exists(F_folder):
                    os.makedirs(F_folder)

                # Create a subfolder with the name of the parent folder of "OutputsDDM"
                subfolder_name = os.path.basename(os.path.dirname(ddm_dir))
                subfolder_path = os.path.join(F_folder, subfolder_name)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)

                # Copy the CSV to the appropriate folder
                shutil.copy(file_path, subfolder_path)
