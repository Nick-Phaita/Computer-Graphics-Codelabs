import os.path
import pandas as pd
from generate_email_addresses import generate_email_addresses
import logging

# File paths
file_path = 'input_files/Test Files.xlsx'
output_folder = 'output_files'

# Set up logging
logging.basicConfig(filename='logs/computation.log', level=logging.INFO)

# Function to log gender statistics
def log_gender_stats(male_count, female_count):
    logging.info(f'Total male students: {male_count}')
    logging.info(f'Total female students: {female_count}')

# Process each sheet in the Excel file
all_sheets = pd.read_excel(file_path, sheet_name=None)
for sheet_name, df in all_sheets.items():
    print(f"Processing Sheet: {sheet_name}")

    # Print column names to verify structure
    print(f"Columns in {sheet_name}: {df.columns}")

    # Ensure 'Gender' column exists before processing
    if 'Gender' not in df.columns:
        print(f"Warning: 'Gender' column not found in {sheet_name}")
        continue  # Skip processing for this sheet if 'Gender' column is missing

    # Strip whitespaces, lowercase 'Gender' values, and replace abbreviations for consistency
    df['Gender'] = df['Gender'].str.strip().str.lower().replace({'m': 'male', 'f': 'female'})

    # Generate emails
    emails = generate_email_addresses(df)
    df['Email'] = emails

    # Separate Male and Female students
    male_students = df[df['Gender'] == 'male']
    female_students = df[df['Gender'] == 'female']

    # Check for empty dataframes and log message if no students found
    if male_students.empty:
        print(f"No male students found in {sheet_name}")
    else:
        male_output_file = os.path.join(output_folder, f'{sheet_name}_male_students.csv')
        male_students.to_csv(male_output_file, index=False)
        print(f"Male students CSV saved to {male_output_file}")

    if female_students.empty:
        print(f"No female students found in {sheet_name}")
    else:
        female_output_file = os.path.join(output_folder, f'{sheet_name}_female_students.csv')
        female_students.to_csv(female_output_file, index=False)
        print(f"Female students CSV saved to {female_output_file}")

    # Log the number of male and female students
    log_gender_stats(len(male_students), len(female_students))

    # Save the updated sheet with emails to CSV file
    csv_output_file = os.path.join(output_folder, f'{sheet_name}_with_emails.csv')
    df.to_csv(csv_output_file, index=False)
    print(f"CSV saved to {csv_output_file}")

    # Save to TSV file (specifying tab as the delimiter)
    tsv_output_file = os.path.join(output_folder, f'{sheet_name}_with_emails.tsv')
    df.to_csv(tsv_output_file, sep='\t', index=False)
    print(f"TSV saved to {tsv_output_file}")
