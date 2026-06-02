from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(filter(str.isalnum, host))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}