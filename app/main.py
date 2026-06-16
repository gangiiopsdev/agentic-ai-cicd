from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if valid_host(host):
        return safe_ping(host)
    else:
        return {'error': 'Invalid host'}, 400

def valid_host(host: str):
    # Add logic to validate the host input
    return True