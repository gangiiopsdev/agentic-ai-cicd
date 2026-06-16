from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.strip() and all(c.isalnum() for c in host) and len(host) <= 255:
        subprocess.call(['ping', host], shell=False)
    else:
        return {'status': 'error', 'message': 'Invalid input'}
    return {'status': 'completed'}