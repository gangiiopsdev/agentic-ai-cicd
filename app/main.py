from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    # Validate host format using regex
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError("Invalid host format")
    ping_cmd = ['ping', '-c', '1', host]  # Limit the number of pings for security
    try:
        result = subprocess.run(ping_cmd, check=True, capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("/ping_safe")
def ping_safe(host: str):
    return safe_ping(host)