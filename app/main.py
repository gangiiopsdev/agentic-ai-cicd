from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    # Execute subprocess safely
    subprocess.call(['ping', host])
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)