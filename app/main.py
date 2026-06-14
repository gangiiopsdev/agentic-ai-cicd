from fastapi import FastAPI
import subprocess

def safe_ping(host):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    subprocess.call(['ping', '--', host])  # Use -- to prevent option injection
    return {'status': 'completed'}