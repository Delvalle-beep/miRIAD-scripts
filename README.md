# miRIAD Data Processing Scripts

This repository contains scripts used to analyze and organize data from the miRIAD (miRNA Expression and Disease Association) database. The scripts automate key steps in data processing, ensuring consistency and facilitating integration with other datasets.

## Features

✔️ **Converts .txt files (comma-separated) into .tsv (tab-separated).**  
✔️ **Merges .tsv files with metadata from SampleSheet.**  
✔️ **Removes unnecessary columns from the final dataset.**  
✔️ **Concatenates multiple .txt and .tsv files into a single total_data.tsv file.**  
✔️ **Calculates summary statistics for expression values (mean, median, min, max, std) of miRNA data** and appends these statistics to the processed files.  
✔️ **Removes duplicate entries based on miRNA_ID** while keeping only the first occurrence, ensuring clean and accurate data.

## Workflow

1️⃣ **Preprocesses raw .txt and .tsv files**: Converts, merges, and structures data into a uniform format.  
2️⃣ **Integrates metadata from SampleSheet**: Combines the raw data with relevant metadata to create a comprehensive dataset.  
3️⃣ **Cleans and formats the dataset**: Removes unnecessary columns and duplicates, ensuring that the dataset is ready for analysis.  
4️⃣ **Calculates statistical metrics**: For miRNA expression levels, such as mean, median, minimum, maximum, and standard deviation.  
5️⃣ **Combines all processed data**: Merges the cleaned data, along with calculated statistics, into a final structured file for downstream analysis.

## Requirements

- Python 3.x  
- Pandas

## Usage


Run the scripts in sequence to process the data efficiently:

```bash
python source_step0.py  
python source_step1.py  
python source_step2.py  
python source_step3.py  
python source_step(n...).py

