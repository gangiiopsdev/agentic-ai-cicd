from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str) -> bool:
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host name")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    status = safe_ping(host)
    return {"status": "completed", "result": status}