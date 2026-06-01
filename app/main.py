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
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE)
        _ping_cache[host] = result.stdout.decode('utf-8')
    return {"status": "completed", "result": _ping_cache[host]}