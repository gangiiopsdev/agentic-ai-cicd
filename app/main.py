from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str) -> bool:
    return host in ('localhost', '127.0.0.1')

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}