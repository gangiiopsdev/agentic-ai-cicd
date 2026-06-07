from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        return None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "invalid host"}