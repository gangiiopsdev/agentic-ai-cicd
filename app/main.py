from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        response = requests.get(f'http://{host}', timeout=5)
        if response.status_code == 200:
            return {'status': 'completed'}
    except requests.RequestException as e:
        print(f'Error pinging {host}: {e}')
    return {'status': 'failed'}