import os
import pandas as pd

# SCRIPT ONLY TO REMOVE DUPLICATES FROM THE SUMMARY STATISTICS FILE.
def remover_duplicatas_e_linhas(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, sep='\t')

    # Remove the first two rows
    df = df.iloc[2:]

    # Remove duplicates based on the 'gene_id' column
    df.drop_duplicates(subset='gene_id', keep='first', inplace=True)
    df.to_csv(caminho_arquivo, sep='\t', index=False)


diretorio_base = '{base_dir}'

for pasta_raiz, _, arquivos in os.walk(diretorio_base):
    for arquivo in arquivos:
        if arquivo.endswith('_statistic.tsv'):
            caminho_arquivo = os.path.join(pasta_raiz, arquivo)
            remover_duplicatas_e_linhas(caminho_arquivo)

#6. Script for Removing Duplicates and Specific Rows from Statistical Files
#Functionality:
#This script processes all .tsv files containing statistical data, removes the first two rows, and removes duplicate entries based on the gene_id column, keeping only the first occurrence for each gene.

#Steps:

#Iterates through the specified directory and its subdirectories to find all files ending with _statistic.tsv.
#For each found file, the script:
#Removes the first two rows of the file.
#Removes any duplicate entries based on the gene_id column, keeping only the first occurrence.
#The modified DataFrame is then saved back to the original file.