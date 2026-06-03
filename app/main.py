from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with full command path
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate and sanitize input before passing to ping
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ping(host)