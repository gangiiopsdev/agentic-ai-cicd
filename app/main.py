from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]{1,100}$', host):
        return {'status': 'error', 'message': 'Invalid host name'}
    result = subprocess.run(['ping', '-c', '1', f'/sbin/ping'], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e}'}