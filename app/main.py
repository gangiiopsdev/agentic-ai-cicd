from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):  # Allow only local host
        subprocess.call(['ping', host])
    return {'status': 'completed'}