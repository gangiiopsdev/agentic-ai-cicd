from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.strip():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}