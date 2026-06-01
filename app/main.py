from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host parameter is safe before using it in the ping command
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        subprocess.call(['ping', '-c', '1', re.escape(host)])  # Use -c and escape the input to prevent injection
    except Exception as e:
        raise ValueError(str(e)) from e

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

def validate_host(host: str) -> bool:
    # Simple validation example, more complex checks can be added
    allowed_hosts = ["example.com", "127.0.0.1"]
    return host in allowed_hosts