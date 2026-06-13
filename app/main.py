from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode()}'

app = FastAPI()

@app.get("/"

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Stronger input validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    return safe_ping(host)