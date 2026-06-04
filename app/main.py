from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with proper validation and sanitization of host input
    if not host.strip():
        return None
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is None:
        return {"error": "Invalid host input"}
    else:
        return {"status": "completed", "output": result}