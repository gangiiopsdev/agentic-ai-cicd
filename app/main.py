from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host or not host.strip().isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, shell=False)
    return {'status': 'completed'}