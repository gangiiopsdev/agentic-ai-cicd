from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    safe_host = ''.join(e for e in host if e.isalnum() or e.isspace())
    output = safe_ping(safe_host)
    return {"status": "completed", "output": output}