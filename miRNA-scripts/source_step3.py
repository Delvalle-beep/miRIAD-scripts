import os
import pandas as pd
from tqdm import tqdm

# Define input and output directories
input_dir = '{your input dir}'
output_dir = '{your output dir}'

# Initialize an empty DataFrame to store combined data
total_data = pd.DataFrame()

# Traverse all directories and subdirectories
for root_dir, _, files in tqdm(os.walk(input_dir), desc='Processing files'):
    for file in files:
        # Check if the file is a .txt or .tsv
        if file.endswith('.txt') or file.endswith('.tsv'):
            file_path = os.path.join(root_dir, file)
            # Read the file (assumes .txt uses tabs, .tsv uses default separator)
            data = pd.read_csv(file_path, sep='\t' if file.endswith('.txt') else None)
            total_data = pd.concat([total_data, data])

# Save the combined data to a single .tsv file
output_path = os.path.join(output_dir, 'total_data.tsv')
total_data.to_csv(output_path, sep='\t', index=False)

#What does this do?

#Purpose: Concatenates all .txt and .tsv files into a single file.

#Step by step:

#Scans all files in the directory.
#Reads each file (assuming .txt files use tabs as separators).
#Merges all DataFrames into a single dados_totais.tsv file.