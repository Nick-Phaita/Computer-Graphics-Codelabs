from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from googleapiclient.http import MediaFileUpload

# Define the scopes (permissions) that we need.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Authenticate and get credentials
def authenticate_google():
    creds = None
    # Check if the token.pickle file exists and load saved credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials, perform OAuth login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Upload a file to Google Drive
def upload_to_drive(filename, filepath, mimetype):
    # Authenticate with Google
    creds = authenticate_google()

    # Build the Google Drive API service
    service = build('drive', 'v3', credentials=creds)

    # Define file metadata
    file_metadata = {'name': filename}

    # Specify the file to upload and its type
    media = MediaFileUpload(filepath, mimetype=mimetype)

    # Upload the file
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # Output the ID of the uploaded file
    print(f"File uploaded successfully! File ID: {file.get('id')}")

# Example Usage
upload_to_drive("main.py", r"C:\Computer-Graphics-Codelabs\main.py", "text/plain")
