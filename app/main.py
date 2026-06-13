from fastapi import FastAPI
import subprocess
def validate_host(host):
    valid_hosts = ['example.com', 'localhost']
    return host in valid_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
    return {'status': 'completed'}