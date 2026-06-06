from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

def validate_host(host):
    # Basic validation for demonstration purposes
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and use of Popen for better control
    validate_host(host)
    result = subprocess.Popen(['ping', '-c', '1', host], stdout=PIPE, stderr=PIPE)
    output, error = result.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}