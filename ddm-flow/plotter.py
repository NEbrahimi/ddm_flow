# This script could be used to plot data for individual filters. A path pointing to the filter folder that was created
# using rearrange-csv-to-filter-folders.py should be defined (e.g., the "F2" folder).


import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory where a specific patient's folders are located
filter_dir = 'C:/Users/z3541106/unsw/analysis/pcd-modulation-megan/analysis-individual-filter/F5'

# Map original folder names to cleaned-up condition names
condition_folders = os.listdir(filter_dir)
conditions = {folder: folder.rsplit('-', 1)[0] for folder in condition_folders if os.path.isdir(os.path.join(filter_dir, folder))}

# A dictionary to hold condition -> {filter: [avg_values]}
data = {}

# Loop through conditions
for folder, condition in conditions.items():
    condition_path = os.path.join(filter_dir, folder)

    # Ensure condition_path is a directory before listing its contents
    if os.path.isdir(condition_path):

        # Loop through CSV files (filters) in the condition folder
        for csv_file in os.listdir(condition_path):
            if csv_file.endswith(".csv"):
                filter_num = int(csv_file.split('-')[-1][1])  # Extracting filter number from the filename
                csv_path = os.path.join(condition_path, csv_file)

                # Read the CSV and compute the mean for each column
                df = pd.read_csv(csv_path)

                # Find the row with "FoV Averages:"
                avg_row_index = df[df.iloc[:, 0] == "FoV Averages:"].index[0]

                # Get the row after that, which contains the averages
                averages = df.iloc[avg_row_index + 1]

                # Store the averages in the data dictionary
                if condition not in data:
                    data[condition] = {}
                data[condition][filter_num] = averages

# Plot the data
conditions = [name.rsplit('-', 1)[0] for name in os.listdir(filter_dir) if os.path.isdir(os.path.join(filter_dir, name))]

filters = sorted(set([f for condition in data.values() for f in condition.keys()]))
x = range(len(conditions))

fig, ax = plt.subplots()
for f in filters:
    for i, condition in enumerate(conditions):
        y_values = data[condition][f].astype(float).tolist()
        x_values = [i] * len(y_values)
        ax.scatter(x_values, y_values, color="purple", label=f'Filter {f}' if condition == conditions[0] else "", alpha=0.7) #Different colours could be used

# Highlight the area from 0 to 30 on the y-axis
ax.axhspan(0, 30, facecolor='0.5', alpha=0.2)

ax.set_ylabel('Frequency (Hz)')
ax.set_title('Average values for 9 FoVs (Suspected PCD: 11-23-115-XX)')
ax.set_xticks(range(len(conditions)))
ax.set_xticklabels(conditions, rotation=45)
ax.legend()

plt.tight_layout()

# Save the scatter plot in the patient's directory
fig.savefig(os.path.join(filter_dir, "averages_plot.png"))

# Close the figure after saving to release memory
plt.close(fig)






