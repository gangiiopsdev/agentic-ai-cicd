from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "error": None
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "output": None,
            "error": str(e)
        }

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host to prevent command injection
    if not host.isalnum() or len(host) > 100:
        return {
            "status": "failed",
            "output": None,
            "error": "Invalid host"
        }
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}