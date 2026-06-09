from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Safer implementation using subprocess.run and list of arguments
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)