from fastapi import FastAPI
import subprocess
global _ping_cache = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in _ping_cache:
        return {"status": "completed", "result": _ping_cache[host]}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        _ping_cache[host] = result.stdout.strip()
        return {"status": "completed", "result": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}