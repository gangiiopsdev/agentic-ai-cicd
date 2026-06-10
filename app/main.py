from fastapi import FastAPI
import subprocess
from typing import Optional

def validate_host(host):
    if host is None:
        return False
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: Optional[str] = None):
    if not validate_host(host):
        return {"error": "Invalid host parameter"}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

    return {"status": "completed"}