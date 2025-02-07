#miRIAD Data Processing Scripts

This repository contains scripts used to analyze and organize data from the miRIAD (miRNA Expression and Disease Association) database. The scripts automate key steps in data processing, ensuring consistency and facilitating integration with other datasets.

Features

✔️ Converts .txt files (comma-separated) into .tsv (tab-separated).✔️ Merges .tsv files with metadata from SampleSheet.✔️ Removes unnecessary columns from the final dataset.✔️ Concatenates multiple .txt and .tsv files into a single dados_totais.tsv file.

Workflow

1️⃣ Preprocesses raw .txt and .tsv files.2️⃣ Integrates metadata from SampleSheet.3️⃣ Cleans and formats the dataset by removing redundant columns.4️⃣ Combines all processed data into a final structured file.

Requirements

Python 3.x

Pandas

Usage

Run the scripts in sequence to process the data efficiently:

python convert_txt_to_tsv.py
python merge_with_metadata.py
python clean_data.py
python concatenate_files.py

Notes

⚠️ Ensure that .txt files use tab separators to avoid errors.⚠️ File names in SampleSheet must match exactly with the corresponding .tsv files.

