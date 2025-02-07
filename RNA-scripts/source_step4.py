import os
import pandas as pd
from tqdm import tqdm

# Function to calculate statistics and save the DataFrame
def calcular_estatisticas_e_salvar(caminho_arquivo):

    df = pd.read_csv(caminho_arquivo, sep='\t')

    # Check if the 'tpm_unstranded' column contains numeric values
    if pd.api.types.is_numeric_dtype(df['tpm_unstranded']):
        media_valores_repetidos = df.groupby('gene_id')['tpm_unstranded'].mean()
        mediana_valores_repetidos = df.groupby('gene_id')['tpm_unstranded'].median()
        minimo_valores_repetidos = df.groupby('gene_id')['tpm_unstranded'].min()
        maximo_valores_repetidos = df.groupby('gene_id')['tpm_unstranded'].max()
        desvio_padrao_valores_repetidos = df.groupby('gene_id')['tpm_unstranded'].std()

        df['mean_reads_per_million'] = df['gene_id'].map(media_valores_repetidos)
        df['median_reads_per_million'] = df['gene_id'].map(mediana_valores_repetidos)
        df['min_reads_per_million'] = df['gene_id'].map(minimo_valores_repetidos)
        df['max_reads_per_million'] = df['gene_id'].map(maximo_valores_repetidos)
        df['std_reads_per_million'] = df['gene_id'].map(desvio_padrao_valores_repetidos)

        nome_arquivo_atual = os.path.basename(caminho_arquivo)

        novo_nome_arquivo = os.path.splitext(nome_arquivo_atual)[0] + '_statistic.tsv'
        novo_caminho_arquivo = os.path.join(os.path.dirname(caminho_arquivo), novo_nome_arquivo)
        df.to_csv(novo_caminho_arquivo, sep='\t', index=False)
    else:
        print(f"Warning: The file '{caminho_arquivo}' does not contain numeric data in the 'tpm_unstranded' column.")

# Base directory
diretorio_base = '{base-dir}'

# Iterate through all directories and subdirectories
for pasta_raiz, _, arquivos in tqdm(os.walk(diretorio_base), desc="Processing files"):
    for arquivo in arquivos:
        if arquivo.endswith('.tsv'):
            caminho_arquivo = os.path.join(pasta_raiz, arquivo)
            calcular_estatisticas_e_salvar(caminho_arquivo)

#5. Script for Calculating Statistics and Saving Data for All .tsv Files
#Functionality:
#This script calculates statistical metrics (mean, median, min, max, std) for the tpm_unstranded column of all .tsv files in the given directory and its subdirectories. The results are then saved to a new file, appending _statistic to the original file name.

#Steps:

#Iterates through all directories and subdirectories in the specified base directory.
#For each .tsv file, the script reads the file, checks if the tpm_unstranded column contains numeric data, and calculates the following statistics:
#Mean of tpm_unstranded per gene_id
#Median of tpm_unstranded per gene_id
#Min value of tpm_unstranded per gene_id
#Max value of tpm_unstranded per gene_id
#Standard deviation of tpm_unstranded per gene_id
#The calculated statistics are then added to the DataFrame, and the result is saved as a new file with _statistic appended to the original file name.
#Progress Tracking:

#The script uses the tqdm library to provide a progress bar while processing the files.