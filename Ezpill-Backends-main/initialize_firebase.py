import os
import django
from firebase_admin import credentials, initialize_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firebaseauth.settings')
django.setup()

# Firebase Admin SDK 초기화
cred = credentials.Certificate({
    "type": os.environ.get('FIREBASE_ACCOUNT_TYPE'),
    "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
    "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
    "auth_uri": os.environ.get('FIREBASE_AUTH_URI'),
    "token_uri": os.environ.get('FIREBASE_TOKEN_URI'),
    "auth_provider_x509_cert_url": os.environ.get('FIREBASE_AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.environ.get('FIREBASE_CLIENT_X509_CERT_URL')
})
initialize_app(cred)

print("Firebase Admin SDK has been initialized.")
