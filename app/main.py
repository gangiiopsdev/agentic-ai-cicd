from fastapi import FastAPI
import subprocess
import re
import shlex
git
app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid hostname"}

    # Secure implementation using Popen with shlex and shell=False
    command = ['ping', host]
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = result.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}