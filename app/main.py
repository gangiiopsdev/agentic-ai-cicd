from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is not None:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
        return {'result': result.stdout}
    else:
        return {'error': 'Invalid host'}