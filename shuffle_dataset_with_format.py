import pandas as pd
import json
from difflib import SequenceMatcher

df = pd.read_excel('merged_edited_records.xlsx')

shuffled_data = df.sample(frac=1).reset_index(drop=False)

def find_special_characters(names):
    is_special_char = names.apply(lambda name: 'yes' if any(char for char in name if not char.isalnum() and not char.isspace() and char != ',') else 'no')
    return is_special_char

shuffled_data['Special Character'] = find_special_characters(shuffled_data['Student Name'])

def is_name_similar(names):
    similar_names_flags = []
    for i, name1 in enumerate(names):
        found_similar = False
        for j, name2 in enumerate(names):
            if i != j and SequenceMatcher(None, name1, name2).ratio() > 0.8:
                found_similar = True
                break
        similar_names_flags.append('yes' if found_similar else 'no')
    return pd.Series(similar_names_flags)


shuffled_data['Name Similar'] = is_name_similar(shuffled_data['Student Name'])

def format_data(row):
    return {
        "No.": str(row['No.']),
        "Student Number": str(row['Student Number']),
        "additional_details": [
            {"DoB": row['DoB'].strftime('%Y-%m-%d') if pd.notnull(row['DoB']) else None},
            {"Gender": row['Gender']},
            {"Special Character": row['Special Character']},
            {"Name Similar": row['Name Similar']}
        ]
    }



formatted_data = shuffled_data.apply(format_data, axis=1).tolist()

destination_file = 'output_files/shuffled_formatted_records.json'

with open(destination_file, 'w') as f:
    json.dump(formatted_data, f, indent=4)

print(f'Kindly check the file named {destination_file}')