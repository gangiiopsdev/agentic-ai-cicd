from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}