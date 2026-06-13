from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}
    args = shlex.split('ping -c 1 ' + host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)