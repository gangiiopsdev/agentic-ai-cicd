from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it is safe to ping
    if not validate_host(host):
        return {"error": "Invalid host", "status": "failed"}
    try:
        subprocess.call(["ping", re.escape(host)])  # Use re.escape to escape any potentially dangerous characters in the host input
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., check for allowed characters and formats
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return re.match(pattern, host) is not None