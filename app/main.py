from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation for demonstration purposes
    return host.strip().replace('.', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}