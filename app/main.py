from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host or '@' in host:
        return {"status": "failed", "error": "Invalid input"}
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}