from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

ALLOWED_HOSTS = {'example.com', 'localhost'}

@app.get('/ping/{host}')
def ping(host: str):
    if not validate_host(host) or host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Invalid host'}
    parsed_url = urlparse(host)
    if parsed_url.scheme or parsed_url.netloc or '@' in host or ':' in host.split('/')[0]:
        return {'status': 'error', 'message': 'Invalid host format'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    return host.isalnum()