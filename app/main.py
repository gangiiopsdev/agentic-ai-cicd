from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid input")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}