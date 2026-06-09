from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, timeout=5)  # Adjust timeout as needed
        return {"status": "completed"}
    except subprocess.TimeoutExpired:
        return {"error": "Command timed out"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}