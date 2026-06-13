from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not is_valid_host(host):
        raise ValueError('Invalid host parameter')
    subprocess.run(['/usr/bin/ping', host], check=True, shell=False)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return True