from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if 'ping' in host or any(char in host for char in [';', '|', '&']):
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)