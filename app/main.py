from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    encoded_host = subprocess.check_output(['echo', shlex.quote(host)]).decode().strip()
    args = ['ping', encoded_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}