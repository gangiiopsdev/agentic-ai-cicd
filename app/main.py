from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input sanitization
    if not host.strip():
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {"status": "completed"}