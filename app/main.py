from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def sanitize_host(host: str) -> bool:
    parsed_url = urlparse(host)
    return not (parsed_url.scheme or parsed_url.netloc)

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}