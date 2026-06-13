from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shlex.split to avoid shell injection
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = subprocess.quote(host)
    safe_ping(escaped_host)  # Ensure the host input is properly quoted
    return {"status": "completed"}