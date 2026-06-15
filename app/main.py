from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input before using it in subprocess
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True, text=True)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ping_result = subprocess.run(['ping', host], check=True, text=True)
        return {"status": "completed", "result": ping_result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}