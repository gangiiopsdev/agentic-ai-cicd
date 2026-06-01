from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use a list for the command and arguments to avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.strip().isdigit() or len(host) > 15:
        return {"status": "Invalid host", "message": "Host must be a valid IP address"}
    result = safe_ping(host)
    return {"status": "completed", "result": result}