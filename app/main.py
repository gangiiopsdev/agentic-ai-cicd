from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    result = subprocess.run(args, check=True, shell=False)
    return result

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping command failed"}