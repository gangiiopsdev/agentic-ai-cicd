from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Regular expression to allow only certain characters in the hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "message": "Invalid hostname"}

    subprocess.call(["ping", host])

    return {"status": "completed"}