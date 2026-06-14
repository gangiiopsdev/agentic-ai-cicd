from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        return subprocess.call(['ping', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        return -1

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == -1:
        return {"error": "Invalid host format"}
    else:
        return {"status": "completed", "result": result}