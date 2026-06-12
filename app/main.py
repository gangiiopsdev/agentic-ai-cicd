from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if host.startswith('192.168.'):
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['.', '-'])
        subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}