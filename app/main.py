from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host to allow only alphanumeric characters and select few special characters.
    if not re.match(r'^[a-zA-Z0-9_.-]{1,}$', host):
        return {"status": "error", "output": "Invalid input"}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}