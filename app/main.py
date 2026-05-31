from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if any(char in host for char in [';', '|', '&', '<', '>', '$']):
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}