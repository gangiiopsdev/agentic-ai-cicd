from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def secure_ping(command):
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return output.decode(), error.decode() if error else None

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid hostname"}

    command = ['ping'] + shlex.split(host)
    output, error = secure_ping(command)
    return {"status": "completed", "output": output, "error": error}