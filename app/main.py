from fastapi import FastAPI
import subprocess

app = FastAPI()

def check_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Unauthorized host')

@app.get('/ping')
def ping(host: str):
    if not check_host(host):
        return {'status': 'error', 'message': 'Unauthorized host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}