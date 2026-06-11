from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    # Validate host input
    if not host or len(host) > 255:
        raise ValueError("Invalid host input")
    # Use a whitelist of allowed hosts for security
    allowed_hosts = ['192.168.1.1', '8.8.8.8']
    if host not in allowed_hosts:
        raise ValueError("Host is not in the allowed list")
    result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)