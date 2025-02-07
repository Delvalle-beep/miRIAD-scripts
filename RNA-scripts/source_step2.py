import pandas as pd

def filter_and_save(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path, sep='\t')

        # Filter the DataFrame
        df_filtered = df[(df['gene_type'] == 'protein_coding') & (df['Sample Type'] == 'Solid Tissue Normal')]

        # Save the filtered result to the same file
        df_filtered.to_csv(file_path, sep='\t', index=False)

        print(f"Filtering completed and result saved to {file_path}.")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

# Path to the file to be processed
file_to_process = '{files-dir}'

# Call the function for the specific file
filter_and_save(file_to_process)

#3. Script for Filtering Data by Gene Type and Sample Type
#Functionality:
#This script filters the RNA-Seq data for a specific gene type (protein_coding) and sample type (Solid Tissue Normal). The filtered data is saved back to the original file.

#Steps:

#Reads the input .tsv file.
#Filters the data based on the conditions: gene_type == 'protein_coding' and Sample Type == 'Solid Tissue Normal'.
#Saves the filtered data back to the same file.