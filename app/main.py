from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid input'}
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)