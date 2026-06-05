from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    if not host.isalnum() or len(host) > 100:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    subprocess.run(["ping", host], check=True, text=True, capture_output=True)
    return {"status": "completed"}