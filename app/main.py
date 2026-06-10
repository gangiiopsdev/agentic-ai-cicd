from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def is_safe_url(url):
    parsed_url = urlparse(url)
    return not (parsed_url.scheme or ':' in parsed_url.netloc or '@' in parsed_url.netloc)

@app.get('/ping')
def ping(host: str):
    if not is_safe_url(host):
        return {'status': 'failed', 'error': 'Unsafe URL provided'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}