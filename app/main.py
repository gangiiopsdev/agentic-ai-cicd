from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}