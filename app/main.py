from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    if re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\. [0-9]{1,3}\. [0-9]{1,3}$', host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "invalid_host"}