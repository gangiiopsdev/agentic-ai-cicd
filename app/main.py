from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return host.isalnum() and '-' not in host

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid input'}, 400
    subprocess.call(['ping', f'127.0.0.1 {host}'], shell=False)
    return {'status': 'completed'}