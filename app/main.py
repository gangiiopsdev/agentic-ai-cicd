from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def validate_input(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    try:
        validate_input(host)
        safe_host = quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}