from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}