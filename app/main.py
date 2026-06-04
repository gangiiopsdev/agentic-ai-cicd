from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        url = urlparse(host)
        if url.scheme or '@' in host or ':' not in host:
            raise ValueError('Invalid input for ping')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}