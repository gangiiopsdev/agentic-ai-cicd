from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here to ensure 'host' is safe
    return host.replace('.', '').isdigit() and len(host) <= 15

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}