from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    if not host.isdigit():
        return False
    subprocess.call(['ping', host])
    return True

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if _ping(host):
        return {"status": "completed"}
    else:
        return {"status": "error", "reason": "Invalid host input"}