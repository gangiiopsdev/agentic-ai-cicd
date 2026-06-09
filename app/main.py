from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'completed'}