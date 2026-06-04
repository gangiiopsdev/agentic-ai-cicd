from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or '.' not in host:
        return {"status": "completed", "result": "Invalid input"}
    try:
        # Safe implementation
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "result": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "completed", "result": str(e)}