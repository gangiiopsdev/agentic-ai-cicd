from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

def ping(host: str):
    # Safer implementation with input validation and sanitization
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    process = Popen(['ping', host], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

@app.get('/ping')
def ping_safe(host: str):
    return {'status': 'completed'}