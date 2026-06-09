from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input
    if 'ping' in host or '&' in host or ';' in host:
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}