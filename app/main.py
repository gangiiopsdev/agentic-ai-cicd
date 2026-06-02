from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement logic to check if the host is safe
    return host in ['127.0.0.1', '::1']

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host specified')
    subprocess.call(['ping', host])
    return {'status': 'completed'}