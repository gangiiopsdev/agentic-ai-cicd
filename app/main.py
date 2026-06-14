from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 10:
        return {"status": "failed", "error": "Invalid host name"}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout
    }