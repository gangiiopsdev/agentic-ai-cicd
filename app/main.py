from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex to safely split the command
    safe_host = shlex.quote(host)
    subprocess.run(f'ping {safe_host}', shell=False, check=True)
    return {"status": "completed"}