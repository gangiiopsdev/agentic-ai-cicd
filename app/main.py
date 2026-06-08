from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent injection attacks
    if not host.isalnum() or len(host) > 100:
        return {"status": "error", "result": "Invalid host input"}
    result = safe_ping(host)
    return {"status": "completed", "result": result}