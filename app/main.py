from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_hostname(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_', '/', ':'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_hostname(host)
    if not sanitized_host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}