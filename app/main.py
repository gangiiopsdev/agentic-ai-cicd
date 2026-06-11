from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    return host.isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host name")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout