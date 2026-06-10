from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize host input to prevent injection attacks
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    subprocess.check_call(['ping', sanitized_host], shell=False)
    return {"status": "completed"}