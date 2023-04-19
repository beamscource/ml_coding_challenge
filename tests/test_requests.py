import requests

url = 'http://0.0.0.0:8000/score'
files = [('files', open('data/test/sandal/Sandal (948).jpg', 'rb'))]
resp = requests.post(url=url, files=files) 
print(resp.json())