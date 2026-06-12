from fastapi import FastAPI
import subprocess
global_ping_cache = {}

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if host not in global_ping_cache:
        global_ping_cache[host] = subprocess.call(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "result": global_ping_cache[host]}