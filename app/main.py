from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    return {'result': safe_ping(host)}