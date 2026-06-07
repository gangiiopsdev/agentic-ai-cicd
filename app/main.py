from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host")
    # Safe implementation using subprocess.run with list of arguments
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}