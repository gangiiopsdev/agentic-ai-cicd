from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host to ensure it is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {"status": "error", "output": "Invalid host"}
        result = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}