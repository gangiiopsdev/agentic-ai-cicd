from fastapi import FastAPI
import subprocess
import re

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def is_valid_hostname(hostname):
    # Regex to validate hostname
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(hostname))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_hostname(host):
        return {"error": "Invalid hostname"}
    status = run_ping(host)
    return {"status": status}