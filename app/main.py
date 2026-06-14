from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and args parameter
    if host.strip() and all(c.isalnum() or c in '-.' for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host input')
    return {'status': 'completed'}