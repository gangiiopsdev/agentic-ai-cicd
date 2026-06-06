from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.strip() and not any(char in host for char in [';', '&', '|', '$']):  # Basic input validation
        subprocess.call(['ping', host])
    return {'status': 'completed'}