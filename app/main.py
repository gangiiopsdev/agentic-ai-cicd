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
        # Validate the input to ensure it's a safe host name or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host.split('.')) > 4:
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

# Helper function to validate the host input
def is_safe_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex, allowed IP ranges)
    return True