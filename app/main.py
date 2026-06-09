from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}