from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(c in valid_chars for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', subprocess.quote(host)], shell=False)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}