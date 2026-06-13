from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):  # Add validation to ensure the host is safe
    if not safe_ping(host):
        return {"status": "error", "message": "Invalid host"}
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}