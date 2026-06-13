from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {"status": "error", "message": "Invalid hostname"}
    try:
        subprocess.run(["ping", host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}