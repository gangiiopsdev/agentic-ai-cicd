from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500