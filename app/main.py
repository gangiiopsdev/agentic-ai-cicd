from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' in host:
        return False
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host) is False:
        return {"error": "Invalid input detected."}
    return {"status": "completed", "output": safe_ping(host)}