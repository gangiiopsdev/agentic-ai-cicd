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
        result = subprocess.call(f'ping -c 1 {host}', shell=True)
        _ping_cache[host] = result
    return {"status": "completed", "result": _ping_cache[host]}