from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[0-9]{1,3}([.][0-9]{1,3}){3}$', host) or len(host) > 15:
        return {"status": "failed", "error": "Invalid host input"}
    try:
        # Use a more secure method to avoid command injection
        output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, timeout=5)
        if output.returncode != 0:
            return {"status": "failed", "error": output.stderr}
        else:
            return {"status": "completed", "output": output.stdout} 
    except subprocess.TimeoutExpired as e:
        return {"status": "failed", "error": str(e)}