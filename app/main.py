from fastapi import FastAPI
import subprocess
import re

given_host = '127.0.0.1' # Replace with a secure source of hostnames

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str): 
    try:
        # Validate the host to prevent command injection
        if not re.match(r'^[0-9]+(?:\.[0-9]+){3}$', host):
            raise ValueError("Invalid IP address")
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}