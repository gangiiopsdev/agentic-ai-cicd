from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid host')