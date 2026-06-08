from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/ping/{host}")
def ping(host: str):
    try:
        # Validate host input to prevent HTTP request injection
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
        if not all(c in allowed_chars for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        response = requests.get(f'http://{host}', timeout=1)
        return {'status': 'completed', 'output': response.status_code}
    except requests.exceptions.RequestException as e:
        return {'status': 'failed', 'error': str(e)}