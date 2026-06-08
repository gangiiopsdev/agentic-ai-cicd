from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_ping(host: str):
    # Safe implementation
    args = ['ping', quote(host)]
    subprocess.run(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}