from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to allow only alphanumeric characters and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {"status": "error", "message": "Invalid hostname"}
    # Secure implementation
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}