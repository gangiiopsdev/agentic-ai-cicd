from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host provided")
    subprocess.run(['ping', subprocess.check_output(['echo', host]).decode('utf-8')], check=True)
    return {"status": "completed"}