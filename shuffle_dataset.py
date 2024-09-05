import pandas as pd

df = pd.read_excel('merged_edited_records.xlsx')

shuffled_data = df.sample(frac=1).reset_index(drop=False)

destination_file = 'output_files/shuffled_records.json'
shuffled_data.to_json(destination_file, orient='records', lines = True)

print(f'Kindly check the file named {destination_file} ')