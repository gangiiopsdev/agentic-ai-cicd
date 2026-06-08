from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host specified')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}