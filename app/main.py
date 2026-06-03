from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use shlex to safely construct the command
    safe_host = host.strip()
    if not all(c.isalnum() or c in '-._' for c in safe_host):
        return {"error": "Invalid characters in host name"}
    command = ["ping", shlex.quote(safe_host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}