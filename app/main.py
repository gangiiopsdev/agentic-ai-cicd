from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the hostname by using shlex.quote
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid hostname')
    safe_ping(host)
    return {'status': 'completed'}