from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if 'ping' in host:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', '-c', '1', host], shell=False)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}