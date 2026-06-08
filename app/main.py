from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    # Validate user input
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}