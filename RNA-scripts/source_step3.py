import os
import pandas as pd

# Root directory to be processed
root_directory = '{root-dir}'

# Function to filter and save files in each folder
def filter_and_save_in_folders(directory):
    # Iterate through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('_statistic.tsv'):
                # Build the full file path
                file_path = os.path.join(root, file)

                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path, sep='\t')

                    # Filter the DataFrame
                    df_filtered = df[df['gene_type'] == 'protein_coding']

                    # Save the result in the same file
                    df_filtered.to_csv(file_path, sep='\t', index=False)

                    print(f"Filtering completed and results saved in {file_path}.")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

# Call the function for each folder and subfolder in the root directory
filter_and_save_in_folders(root_directory)


#4. Script for Filtering and Saving Protein-Coding Gene Data in Each Folder
#Functionality:
#This script filters all _statistic.tsv files in a given directory and its subdirectories. It retains only the entries with gene_type equal to protein_coding and saves the filtered results back to the same file.

#Steps:

#Iterates through all folders and subfolders in the specified root directory.
#For each _statistic.tsv file found, the script reads the data, filters for rows where the gene_type is protein_coding, and saves the filtered data back to the file.
#Prints the status of each file processed.