from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and escaping
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "result": "Invalid host"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "result": str(e)}