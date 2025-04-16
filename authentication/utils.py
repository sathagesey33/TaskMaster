import requests
import urllib
import jwt
from django.conf import settings


def get_id_token_with_code(code):
    """
    Exchange the authorization code for an ID token.
    """
    
    token_endpoint = "https://oauth2.googleapis.com/token"
    payload = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        # 'redirect_uri': "postmessage", # This is when loading it using javascript
        'redirect_uri': 'http://localhost:8000/auth/callback/',  # Change this to your redirect URI
        'grant_type': 'authorization_code'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = urllib.parse.urlencode(payload)

    response = requests.post(token_endpoint, data=body, headers=headers)

    if response.status_code == 200:
        id_token = response.json().get('id_token')
        return jwt.decode(id_token, options={"verify_signature": False})
    else:
        raise Exception("Failed to obtain ID token from Google: " + response.text)