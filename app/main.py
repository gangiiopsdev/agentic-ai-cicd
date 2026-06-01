from fastapi import FastAPI
import subprocess
global _ping_cache {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in _ping_cache:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        _ping_cache[host] = result.returncode
    return {"status": "completed", "result": _ping_cache[host]}