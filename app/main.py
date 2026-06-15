from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}, 400
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {"status": "completed"}