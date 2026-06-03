from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

def secure_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Secure implementation using the full executable path
    result = subprocess.run(['/bin/ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)