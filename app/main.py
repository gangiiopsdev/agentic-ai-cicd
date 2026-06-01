from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    output = safe_ping(host)
    return {"status": "completed", "output": output}

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ["127.0.0.1", "localhost"]
    return host in allowed_hosts