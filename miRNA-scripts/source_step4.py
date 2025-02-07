import os
import pandas as pd

# GIVEN THAT THERE ARE MULTIPLE DUPLICATE miRNA VALUES WITH DIFFERENT EXPRESSION LEVELS
# I will calculate statistics for unique miRNA value groups.
# Min, max, mean, median, and standard deviation. The code will currently keep duplicate values.

def calculate_statistics_and_save(file_path):

    df = pd.read_csv(file_path, sep='\t')

    # Check if the 'reads_per_million_miRNA_mapped' column contains numeric values
    if pd.api.types.is_numeric_dtype(df['reads_per_million_miRNA_mapped']):
        mean_repeated_values = df.groupby('miRNA_ID')['reads_per_million_miRNA_mapped'].mean()
        median_repeated_values = df.groupby('miRNA_ID')['reads_per_million_miRNA_mapped'].median()
        min_repeated_values = df.groupby('miRNA_ID')['reads_per_million_miRNA_mapped'].min()
        max_repeated_values = df.groupby('miRNA_ID')['reads_per_million_miRNA_mapped'].max()
        std_repeated_values = df.groupby('miRNA_ID')['reads_per_million_miRNA_mapped'].std()

        df['mean_reads_per_million'] = df['miRNA_ID'].map(mean_repeated_values)
        df['median_reads_per_million'] = df['miRNA_ID'].map(median_repeated_values)
        df['min_reads_per_million'] = df['miRNA_ID'].map(min_repeated_values)
        df['max_reads_per_million'] = df['miRNA_ID'].map(max_repeated_values)
        df['std_reads_per_million'] = df['miRNA_ID'].map(std_repeated_values)

        current_file_name = os.path.basename(file_path)

        new_file_name = os.path.splitext(current_file_name)[0] + '_statistic.tsv'
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        df.to_csv(new_file_path, sep='\t', index=False)
    else:
        print(f"Warning: The file '{file_path}' does not contain numeric data in the 'reads_per_million_miRNA_mapped' column.")

# Base directory
base_directory = '/home/scratch45-3/voliveira_17_jun/expression-files/miRNA-seq/final-data/'

# Traverse all directories and subdirectories
for root_folder, _, files in os.walk(base_directory):
    for file in files:
        if file.endswith('.tsv'):
            file_path = os.path.join(root_folder, file)
            calculate_statistics_and_save(file_path)

#5. Script for Calculating Statistics on miRNA Data
#Functionality:
#This script processes .tsv files containing miRNA expression data, calculates summary statistics (mean, median, min, max, and standard deviation) for each unique miRNA_ID, and appends these values as new columns in the original dataset. It then saves the updated data to a new file.

#Steps:

#Iterates through the specified directory and its subdirectories to find all files ending with .tsv.
#For each file, it:
#Groups the data by miRNA_ID and computes:
#Mean, median, min, max, and standard deviation of reads_per_million_miRNA_mapped.
#Adds these statistical values as new columns in the DataFrame.
#Saves the modified DataFrame to a new file with the suffix _statistic.tsv.