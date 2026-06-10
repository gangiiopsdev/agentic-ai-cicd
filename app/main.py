from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"})
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 100:
        return {"error": "Invalid hostname"}, 400

    # Use subprocess.run for better control over the process
    result = subprocess.run([
        'ping',
        host,
    ], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout
    }