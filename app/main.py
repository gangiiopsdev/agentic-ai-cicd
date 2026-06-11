from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        # Sanitize the host parameter using urlparse to prevent injection attacks
        result = subprocess.run(['ping', urlparse(host).hostname], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}