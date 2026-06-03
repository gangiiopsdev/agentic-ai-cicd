from fastapi import FastAPI
import re
import subprocess
def safe_ping(host: str):
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
        return {"status": status}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}