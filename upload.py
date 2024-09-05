from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from googleapiclient.http import MediaFileUpload


SCOPES = ['https://www.googleapis.com/auth/drive.file']
 
def authenticate_google():
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
        
            flow = InstalledAppFlow.from_client_secrets_file(
                'client.secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

    
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def upload_to_drive(filename, filepath, mimetype):
    
    creds = authenticate_google()

    
    service = build('drive', 'v3', credentials=creds)


    file_metadata = {'name': filename}


    media = MediaFileUpload(filepath, mimetype=mimetype)

    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    
    print(f"File uploaded successfully! File ID: {file.get('id')}")


upload_to_drive("main.py", r"C:\Computer-Graphics-Codelabs\main.py", "text/plain")
