from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isdigit() or len(host) > 15:
        return {"status": "error", "message": "Invalid host parameter"}
    result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {
        "status": "completed",
        "stdout": result.stdout.decode(),
        "stderr": result.stderr.decode()
    }