from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 128:
        return {"status": "failed", "error": "Invalid hostname provided"}
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)