from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}