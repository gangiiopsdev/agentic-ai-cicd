from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def safe_ping(host):
    # More robust regex for host validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate the host to ensure it only contains safe characters
        raise ValueError("Invalid host input")
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": safe_ping(host)}