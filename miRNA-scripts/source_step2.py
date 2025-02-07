import pandas as pd

# Read the TSV file containing the total data
df = pd.read_csv('total_data.tsv', sep='\t')

# Drop unnecessary columns
df = df.drop(['id', 'submitter_id', 'entity_type', 'entity_id', 'category',
              'classification', 'created_datetime', 'status', 'notes'], axis=1)

# Save the cleaned data back to the TSV file
df.to_csv('total_data.tsv', sep='\t', index=False)

#What does this do?

#Purpose: Removes unnecessary columns from the combined DataFrame.

#Step by step:

#Reads the dados_totais.tsv file.
#Removes specific columns (e.g., id, submitter_id).
#Saves the modified DataFrame.