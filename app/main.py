from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure host is a valid IP address or hostname
    if not host.replace('.', '', 3).isdigit() and not host.replace('-', '').isalnum():
        raise ValueError("Invalid host")
    subprocess.run(['/usr/bin/ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}