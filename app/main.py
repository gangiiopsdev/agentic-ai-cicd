from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex to safely handle arguments
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(shlex.quote(host))
    return {"status": "completed"}