from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host], shell=False)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}