from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid input"}

    try:
        subprocess.run(['ping', shlex.quote(host)], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}