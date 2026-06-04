from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^([0-9]|[1-9][0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', host):
        return {"status": "error", "message": "Invalid host address"}
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return {"status": "completed"}