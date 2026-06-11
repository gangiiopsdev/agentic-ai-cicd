from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure the host parameter is safe
    if not isinstance(host, str) or '@' in host:
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)