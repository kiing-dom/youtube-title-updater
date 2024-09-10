import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_SECRETS_FILE = os.getenv('CLIENT_SECRETS_FILE', 'client_secrets.json')
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"