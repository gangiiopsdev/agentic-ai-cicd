from fastapi import FastAPI
import subprocess
import re

def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters (e.g., alphanumeric and dots)
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host input")
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get="/ping")
def ping_route(host: str):    return ping(host)

@app.get="/"
def home():    return {"message": "Agentic Self-Healing Pipeline"}