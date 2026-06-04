from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c == '.')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if '.' not in sanitized_host and len(sanitized_host) != len(host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}