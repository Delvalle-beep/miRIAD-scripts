import pandas as pd
import os

# File paths
sample_sheet_path = '{samplesheet-dir}'
data_dir = '{data-dir}'

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

# Iterate over rows in the sample sheet
for index, row in sample_sheet.iterrows():
    file_id = row['File ID']
    file_name = row['File Name']
    project_id = row['Project ID']
    case_id = row['Case ID']
    sample_id = row['Sample ID']
    sample_type = row['Sample Type']

    # Find the matching .tsv file
    tsv_file_path = find_tsv_file(file_id, file_name)

    if tsv_file_path:
        # Read the .tsv file and add metadata columns
        df = pd.read_csv(tsv_file_path, sep='\t')
        df['Project ID'] = project_id
        df['Case ID'] = case_id
        df['Sample ID'] = sample_id
        df['Sample Type'] = sample_type
        relations.append(df)
    else:
        print(f"TSV file not found for File ID: {file_id}")

# Combine all data into a single file
if not relations:
    print("No TSV files found.")
else:
    combined_df = pd.concat(relations, ignore_index=True)
    output_file_path = '{combined-data-dir}'
    combined_df.to_csv(output_file_path, sep='\t', index=False)

#What does this do?

#Purpose: Combines .tsv files with metadata from the SampleSheet.

#Step by step:

#   Reads the SampleSheet (a metadata file containing information such as sample ID, type, etc.).
#   For each row in the SampleSheet, finds the corresponding .tsv file.
#   Adds columns from the SampleSheet (e.g., Project ID, Sample Type) to the .tsv DataFrame.
#Merges all DataFrames into a single file: combined_data.tsv.
#Notes:

#   The function find_tsv_file searches for .tsv files by name (file.startswith(file_name)). Ensure that the names in the SampleSheet match the file names exactly.
#   If there are name inconsistencies, some files may not be found.