from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return host.isalnum() and '-' in host and '.' not in host

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid input')
    args = ['ping', f'-c 1 {host}']
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}