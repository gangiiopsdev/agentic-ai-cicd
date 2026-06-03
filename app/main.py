from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to prevent command injection
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)