from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and len(host) <= 3:
        return subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}