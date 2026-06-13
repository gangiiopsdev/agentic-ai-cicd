from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with args instead of shell=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid input'
    return safe_ping(host)