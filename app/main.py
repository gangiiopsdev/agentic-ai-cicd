from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def is_safe_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@app.get('/ping')
def ping(host: str):
    if not is_safe_url(host) or host.startswith('localhost') or host.startswith('127.0.0.1'):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode()}