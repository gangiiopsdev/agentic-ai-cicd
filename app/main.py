from fastapi import FastAPI
import subprocess
import re


def ping(host: str):
    # Sanitize input to prevent shell injection
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError("Invalid input")
    args = ['ping', re.sub(r'[^a-zA-Z0-9]', '', host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout


global app
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}