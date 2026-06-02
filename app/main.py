from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid host"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'status' in result:
        return result
    # Safe implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}