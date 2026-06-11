from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    cmd = ['ping', host]
    return subprocess.run(cmd)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    safe_host = subprocess.quote(host)
    result = subprocess.run(['ping', safe_host])
    return {"status": "completed", "returncode": result.returncode}