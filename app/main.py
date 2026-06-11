from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to allow only alphanumeric and hyphen characters
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {"status": "failed", "error": "Invalid input. Only alphanumeric and hyphen characters are allowed."}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}