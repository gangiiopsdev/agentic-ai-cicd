from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"遏)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '.' in host:
        return {"status": "failed", "error": "Invalid host parameter"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}