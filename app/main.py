from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return 'Invalid host'
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return 'Ping failed'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}