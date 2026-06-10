from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        return {
            "status": "error",
            "message": "Invalid host input"
        }
    result = safe_ping(host)
    return {
        "status": "completed",
        "output": result.stdout,
        "errors": result.stderr
    }