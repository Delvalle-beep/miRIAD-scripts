# -*- coding: utf-8 -*-
import pandas as pd
import os

def calculate_statistics_and_save(file_path):

    df = pd.read_csv(file_path, sep='\t')

    # Check if the 'tpm_unstranded' column contains numeric values
    if pd.api.types.is_numeric_dtype(df['tpm_unstranded']):
        mean_values = df.groupby('gene_id')['tpm_unstranded'].mean()
        median_values = df.groupby('gene_id')['tpm_unstranded'].median()
        min_values = df.groupby('gene_id')['tpm_unstranded'].min()
        max_values = df.groupby('gene_id')['tpm_unstranded'].max()
        std_values = df.groupby('gene_id')['tpm_unstranded'].std()

        df['mean_reads_per_million'] = df['gene_id'].map(mean_values)
        df['median_reads_per_million'] = df['gene_id'].map(median_values)
        df['min_reads_per_million'] = df['gene_id'].map(min_values)
        df['max_reads_per_million'] = df['gene_id'].map(max_values)
        df['std_reads_per_million'] = df['gene_id'].map(std_values)

        current_file_name = os.path.basename(file_path)

        new_file_name = os.path.splitext(current_file_name)[0] + '_statistic.tsv'
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        df.to_csv(new_file_path, sep='\t', index=False)
    else:
        print(f"Warning: The file '{file_path}' does not contain numeric data in the 'tpm_unstranded' column.")

# Path to the file to be processed
file_path = '{file-path}'

# Call the function for the specific file
calculate_statistics_and_save(file_path)


#2. Script for Calculating Summary Statistics for a Single RNA-Seq Data File
#Functionality:
#This script calculates summary statistics (mean, median, min, max, and standard deviation) for a single RNA-Seq data file, based on the tpm_unstranded column. The statistics are grouped by gene_id, and new columns with these statistics are added to the file.

#Steps:

#Reads the input .tsv file.
#Verifies if the column tpm_unstranded contains numeric values.
#Calculates summary statistics for each gene_id in the tpm_unstranded column.
#Saves the updated data file with the calculated statistics.