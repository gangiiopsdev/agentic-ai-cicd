from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid input"}, 400
    sanitized_host = shlex.quote(host)
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500