from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Define allowed hosts to prevent command injection
ALLOWED_HOSTS = ['example.com', 'localhost']

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Secure implementation using subprocess.run with shell=False and list of arguments
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)