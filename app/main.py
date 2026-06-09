from fastapi import FastAPI
import subprocess
global_hosts = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        return {"status": "denied", "reason": "Host not allowed"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Add allowed hosts to the set
global_hosts.update(['127.0.0.1', 'localhost'])