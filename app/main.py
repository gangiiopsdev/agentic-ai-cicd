from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"\)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not host.isalnum() and not host.replace('.', '', 1).isdigit():
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr}