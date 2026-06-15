from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in [".", "/", "-"] for c in host):
        return {"error": "Invalid host name"}
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(args)
    return {"status": "completed"}