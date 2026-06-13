from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid hostname"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}