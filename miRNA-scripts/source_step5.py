import os
import pandas as pd

# SCRIPT TO REMOVE DUPLICATES FROM THE SUMMARY STATISTICS FILE.
def remove_duplicates(file_path):

    df = pd.read_csv(file_path, sep='\t')
    df.drop_duplicates(subset='miRNA_ID', keep='first', inplace=True)
    df.to_csv(file_path, sep='\t', index=False)

base_directory = '/home/scratch45-3/voliveira_17_jun/expression-files/miRNA-seq/final-data/'

for root_folder, _, files in os.walk(base_directory):
    for file in files:
        if file.endswith('_statistic.tsv'):
            file_path = os.path.join(root_folder, file)
            remove_duplicates(file_path)

#This script scans the directory for files ending in "_statistic.tsv", removes duplicate rows based on the miRNA_ID column (keeping only the first occurrence), and saves the cleaned file.

#6. Script for Removing Duplicates from miRNA Summary Statistics Files
#Functionality:
#This script removes duplicate rows in the miRNA summary statistics files based on the miRNA_ID column. It keeps only the first occurrence of each miRNA_ID and saves the cleaned data back to the file.

#Steps:

#The script scans a specified directory and its subdirectories for files ending with _statistic.tsv.
#For each file:
#Reads the file into a DataFrame.
#Removes duplicate rows based on the miRNA_ID column, keeping the first occurrence.
#Saves the cleaned data back to the same file.
