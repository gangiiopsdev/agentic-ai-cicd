from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host specified')
    subprocess.run(['ping', f'--{host}'], check=True)
    return {'status': 'completed'}