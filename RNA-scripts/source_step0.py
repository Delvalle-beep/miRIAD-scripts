import pandas as pd
import os

# File paths
sample_sheet_path = '{sample_sheet_path}'
data_dir = '{data_dir}'

# Read the sample sheet
sample_sheet = pd.read_csv(sample_sheet_path, sep='\t')

# Function to find the corresponding .tsv file
def find_tsv_file(file_id, file_name):
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.tsv') and file.startswith(file_name):
                return os.path.join(root, file)
    return None

# List to store matched data
relations = []

# Iterate over rows of the DataFrame
for index, row in sample_sheet.iterrows():
    file_id = row['File ID']
    file_name = row['File Name']
    project_id = row['Project ID']
    case_id = row['Case ID']
    sample_id = row['Sample ID']
    sample_type = row['Sample Type']

    # Find the corresponding .tsv file
    tsv_file_path = find_tsv_file(file_id, file_name)

    if tsv_file_path:
        # Add metadata columns to DataFrame
        df = pd.read_csv(tsv_file_path, sep='\t', header=1)
        df['Project ID'] = project_id
        df['Case ID'] = case_id
        df['Sample ID'] = sample_id
        df['Sample Type'] = sample_type

        # Append the DataFrame to the list
        relations.append(df)
    else:
       print("No .tsv file found for File ID:", file_id, "and File Name:", file_name)

# Check if any .tsv files were found
if not relations:
    print("No .tsv files found.")
else:
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(relations, ignore_index=True)

    # Save the resulting DataFrame to a single file
    output_dir = '{output_dir}'
    output_file_path = os.path.join(output_dir, 'combined_data.tsv')
    combined_df.to_csv(output_file_path, sep='\t', index=False)
    print("Combined .tsv file saved to:", output_file_path)

#1. Script for Merging RNA-Seq Sample Sheets with Corresponding .tsv Files
#Functionality:
#This script merges a sample sheet with corresponding RNA-Seq data files (.tsv) by finding the correct .tsv file for each entry in the sample sheet, adding metadata (such as Project ID, Case ID, Sample ID, and Sample Type), and combining the data into a single file.

#Steps:

#Reads the sample sheet (gdc_sample_sheet.2024-05-10.tsv) containing metadata like File ID, File Name, and Sample Type.
#Finds the corresponding .tsv file for each entry by matching File ID and File Name.
#Reads the .tsv files, extracts data, and adds additional metadata columns (e.g., Project ID, Case ID).
#Combines all the individual .tsv data into one large combined_data.tsv file.
#Saves the resulting combined file.