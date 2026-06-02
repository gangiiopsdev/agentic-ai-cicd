from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input to ensure it's a valid hostname or IP address
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args)

def validate_host(host: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}