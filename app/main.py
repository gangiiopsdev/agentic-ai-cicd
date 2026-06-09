from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent shell injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host"
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host"
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)