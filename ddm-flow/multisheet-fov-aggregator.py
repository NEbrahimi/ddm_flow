#The script will automatically generate a CSV file within the associated OutputsDDM subfolder. This holds true
# regardless of the number of subfolders present. Each CSV file contains columns for different Fields of View (FoVs)
# sourced from various sheets in the DDM Excel document. A header labeled "FoV Averages" is added.
# Following this header is a row displaying the average of each column, representing the average for each FoV.


import pandas as pd
import os

# Specify parent directory
parent_dir = 'C:/Users/z3541106/unsw/analysis/pcd-modulation-megan'

# Specify the sheet names you want to read
#sheets_to_read = ["CBFfromDDMFile1", "CBFfromDDMFile2", "CBFfromDDMFile3", "CBFfromDDMFile4", "CBFfromDDMFile5", "CBFfromDDMFile6", "CBFfromDDMFile7", "CBFfromDDMFile8", "CBFfromDDMFile9"]

# Iterate over all subdirectories in the parent directory
for subdir, dirs, files in os.walk(parent_dir):
    # Filter for subdirectories that contain an "OutputsDDM" directory
    if "OutputsDDM" in dirs:
        ddm_dir = os.path.join(subdir, "OutputsDDM")
        for file in os.listdir(ddm_dir):
            if file.endswith(".xlsx"):
                file_path = os.path.join(ddm_dir, file)

                # Get all sheet names in the Excel file
                with pd.ExcelFile(file_path) as xls:
                    all_sheet_names = xls.sheet_names

                # Filter the sheet names to keep only those that start with "CBFfromDDMFile"
                sheets_to_read = [sheet for sheet in all_sheet_names if sheet.startswith("CBFfromDDMFile")]

                # Create an empty DataFrame to store the data
                df = pd.DataFrame()

                # Iterate over the sheets
                for sheet in sheets_to_read:
                    # Read the sheet into a DataFrame
                    sheet_df = pd.read_excel(file_path, sheet_name=sheet, usecols="A", skiprows=0, nrows=12,names=[sheet])

                    # Append the data to the main DataFrame
                    df = pd.concat([df, sheet_df], axis=1)

                # Define the output CSV file path
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                base_name = base_name.replace("DDMOutputsSummary", "").replace("-00_", "")
                output_csv = os.path.join(ddm_dir, "Filter-FoV-Average-test-2" + base_name + ".csv")

                # Write the DataFrame to a CSV file
                df.to_csv(output_csv, index=False)

                # Read the data from the CSV file
                df = pd.read_csv(output_csv)

                # Compute the average of each column
                averages = df.mean()

                # Create a DataFrame with "FoV average" and computed average values
                average_df = pd.DataFrame(columns=df.columns)
                average_df.loc[0] = ["FoV Averages:"] + [None] * (len(df.columns) - 1)
                average_df.loc[1] = averages.values

                # Save the updated DataFrame to CSV
                df = pd.concat([df, average_df], ignore_index=True)
                df.to_csv(output_csv, index=False)

