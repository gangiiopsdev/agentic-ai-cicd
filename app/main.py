from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip():
        raise ValueError('Host parameter is required')
    if any(char in host for char in [';', '&', '|', '>', '<', '*', '?']):  # Basic validation of command injection
        raise ValueError('Invalid characters in host parameter')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host], shell=False)

    return {"status": "completed"}