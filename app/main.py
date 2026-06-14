from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input using regex and shell=True to handle special characters
    sanitized_host = shlex.quote(host)
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, shell=False)  # Removed shell=True
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}