from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    if not host.isalnum() or len(host) > 64:
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}