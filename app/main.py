from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = re.sub(r'[^a-zA-Z0-9-_]', '', host)
    if not safe_host:
        raise ValueError("Invalid input")
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}