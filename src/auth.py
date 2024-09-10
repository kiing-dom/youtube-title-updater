import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import google_auth_oauthlib.flow
import googleapiclient.discovery
from config import CLIENT_SECRETS_FILE, SCOPES, API_SERVICE_NAME, API_VERSION

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
    
    credentials = flow.run_local_server(port=0)
    
    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )