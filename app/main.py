from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not host.strip():
        raise ValueError('Host parameter is required')
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}