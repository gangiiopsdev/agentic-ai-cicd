from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}