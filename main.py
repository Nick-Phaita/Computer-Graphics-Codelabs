import os.path

import pandas as pd
from generate_email_addresses import generate_email_addresses

file_path = 'input_files/Test Files.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)
for sheet_name, df in all_sheets.items():
    print(f"Processing Sheet: {sheet_name}")

    emails = generate_email_addresses(df)
    df['Email'] = emails

    csv_output_file = os.path.join('output_files', f'{sheet_name}_with_emails.csv')
    df.to_csv(csv_output_file, index=False)
    print(f"CSV saved to {csv_output_file}")

    # Save to TSV file (specifying tab as the delimiter)
    tsv_output_file = os.path.join('output_files', f'{sheet_name}_with_emails.tsv')
    df.to_csv(tsv_output_file, sep='\t', index=False)
    print(f"TSV saved to {tsv_output_file}")

import logging

logging.basicConfig(filename='logs/computation.log', level=logging.INFO)

def log_gender_stats(male_count, female_count):
    logging.info(f'Total male students: {male_count}')
    logging.info(f'Total female students: {female_count}')

