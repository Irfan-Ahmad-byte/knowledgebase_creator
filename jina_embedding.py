import requests

url = 'https://api.jina.ai/v1/embeddings'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer jina_0eb59f650ef0429b8c4794cf56d1e5cdrL06maE_iACP6R3AKnJc_dEAszf2'
}

data = {
  'input': ["Your text string goes here", "You can send multiple texts"],
  'model': 'jina-embeddings-v2-base-en'
}

response = requests.post(url, headers=headers, json=data)
