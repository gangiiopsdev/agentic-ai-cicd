from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', host]  # Remove shlex.split to avoid shell injection
    return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}