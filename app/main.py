from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid host name')
    # Using Popen and passing args separately to avoid shell=True
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}