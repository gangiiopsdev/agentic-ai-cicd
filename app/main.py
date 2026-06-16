from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Safe implementation using subprocess.run with validation
    if host.isalnum() and len(host) <= 64:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}