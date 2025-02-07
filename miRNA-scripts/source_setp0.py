import os

def convert_txt_to_tsv(directory):
    # Iterate over all files and folders in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                # Build the full path of the .txt file
                txt_file_path = os.path.join(root, file)

                # Build the full path of the .tsv file
                tsv_file_path = os.path.splitext(txt_file_path)[0] + '.tsv'

                # Check if the .tsv file already exists
                if os.path.exists(tsv_file_path):
                    print(f"TSV file already exists for: {txt_file_path}")
                else:
                    try:
                        # Open the .txt file for reading and the .tsv file for writing
                        with open(txt_file_path, 'r') as txt_file, open(tsv_file_path, 'w') as tsv_file:
                            # Convert each line from .txt to .tsv format
                            for line in txt_file:
                                tsv_file.write(line.replace(',', '\t'))  # Replace commas with tabs
                        print(f"TSV file created for: {txt_file_path}")
                    except Exception as e:
                        print(f"Failed to convert file {txt_file_path}: {e}")

#What does this do?

#Purpose: Converts .txt files (comma-separated) to .tsv files (tab-separated).

#Step by step:

#   Scans all files in the specified directory (and subdirectories).
#   For each .txt file, replaces commas with tabs and saves it as a .tsv file.
#   Checks if the .tsv file already exists to prevent overwriting.
#Notes:

#   Assumes that .txt files use commas as separators. If there are commas within the data (e.g., in text fields), this may cause issues.
#   Useful for standardizing data format for integration with SampleSheet.