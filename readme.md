# Email Generation and Student Data Processing

## Project Overview
This project generates email addresses for students based on their names, ensures email uniqueness, separates students by gender, and logs key statistics. The data is shuffled and saved in various formats such as TSV, CSV, JSON, and JSONL.

## Features
- Email generation based on student names
- Separation of male and female students
- Special character name detection
- Random shuffling of students
- Logging of key metrics

## Project Structure
- `functions.py`: Contains core functions
- `constraints.py`: Contains constraints such as regex patterns
- `main.py`: Main execution file

## Dependencies
- pandas
- openpyxl
- regex
- google-api-python-client

## How to Run
1. Set up the environment using `venv` or `conda`.
2. Run `main.py` to execute the program.
