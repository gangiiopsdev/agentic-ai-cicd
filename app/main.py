from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.ping_cmd = ['ping', '-c', '1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid hostname"}
    try:
        # Use subprocess.run instead of subprocess.call for better error handling and security
        result = subprocess.run(SafePinger.ping_cmd + [host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": str(e),
            "output": e.stderr
        }