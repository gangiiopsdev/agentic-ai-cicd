from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}