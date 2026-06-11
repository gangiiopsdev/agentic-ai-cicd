from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using a list for args instead of shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum() or '.' in host:
        return {"status": "error", "message": "Invalid host name"}
    safe_ping(host)
    return {"status": "completed"}