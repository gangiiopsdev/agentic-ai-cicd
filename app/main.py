from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validation of input
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        return {"status": "error", "message": "Invalid hostname"}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {"status": "completed", "output": result.stderr}
    else:
        return {"status": "completed", "output": result.stdout}