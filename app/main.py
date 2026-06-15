from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to avoid execution of untrusted commands
    if not host.isalnum() or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}