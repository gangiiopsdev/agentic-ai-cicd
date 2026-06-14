from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation to avoid shell injection
    if 'ping' not in host:
        subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}