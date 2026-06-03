from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}