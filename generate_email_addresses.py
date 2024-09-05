"""This python module generates email addresses based on the following specifications:
- mail addresses should be unique
- use two names if available
- no special characters in an email address
"""
from typing import List
import pandas as pd
import re

def generate_email_addresses(df: pd.DataFrame) -> List[str]:
    """Generate unique email addresses from a DataFrame of student names."""
    emails = []
    seen_emails = set()

    for name in df['Student Name']:
        # Split the name into last name and first/middle names
        if ',' in name:
            last_name, first_middle_names = name.split(',', 1)
        else:
            # In case the name is not formatted as expected
            last_name, first_middle_names = name, ""

        # Remove extra spaces and split the first and middle names
        first_middle_names = first_middle_names.strip().split()

        # Extract the first letter of the first name
        if len(first_middle_names) > 0:
            first_name_letter = first_middle_names[0][0]
        else:
            first_name_letter = ''  # Handle cases where first/middle names are missing

        # Clean the last name and first name letter by removing non-alphanumeric characters
        last_name_clean = re.sub(r'[^a-zA-Z0-9]', '', last_name.strip())
        first_name_letter_clean = re.sub(r'[^a-zA-Z0-9]', '', first_name_letter)

        # Construct the email (first letter of first name + last name)
        email = f"{first_name_letter_clean}{last_name_clean.strip()}@gmail.com".lower()

        # Ensure uniqueness by appending a number if necessary
        if email in seen_emails:
            counter = 1
            new_email = f"{email.split('@')[0]}{counter}@gmail.com"
            while new_email in seen_emails:
                counter += 1
                new_email = f"{email.split('@')[0]}{counter}@gmail.com"
            email = new_email

        seen_emails.add(email)
        emails.append(email)

    return emails
