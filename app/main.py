from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        parsed_url = urlparse(host)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError('Invalid host format')
        output = subprocess.check_output(['ping', '-c', '1', parsed_url.netloc], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}