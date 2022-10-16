import json
import requests
from flask_babel import _
from app import app

IAM_TOKEN = app.config['IAM_TOKEN']
folder_id = 'b1gbqr5l6sedjknn2al2'
#texts = ["Hello", "World"]



headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}

def translate(text):
    if 'IAM_TOKEN' not in app.config or \
            not app.config['IAM_TOKEN']:
        return _('Error: the translation service is not configured.')
    
    body = {
    "targetLanguageCode": 'ru',
    "texts": text,
    "folderId": folder_id,
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
    json = body,
    headers = headers
    )
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    print(json.loads(response.content.decode('utf-8-sig'))['translations'][0]['text'])
    return json.loads(response.content.decode('utf-8-sig'))['translations'][0]['text']