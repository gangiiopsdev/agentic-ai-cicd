from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        subprocess.call(['ping', host])
    else:
        return {"error": "Invalid hostname"}
    return {"status": "completed"}