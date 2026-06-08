from fastapi import FastAPI
import subprocess
import re

# Regular expression for validating an IP address
IP_REGEX = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

def safe_ping(host: str):
    # Ensure the host input is sanitized or validated
    if not re.match(IP_REGEX, host) and not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', f'-c 1 {host}'], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}