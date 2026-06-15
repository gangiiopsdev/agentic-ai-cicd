from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {"status": "invalid input"}

    subprocess.run(['ping', host], shell=False)
    return {"status": "completed"}