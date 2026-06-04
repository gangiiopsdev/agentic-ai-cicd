from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Simple validation example, replace with more robust logic
    return '.' in host