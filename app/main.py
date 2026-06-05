from fastapi import FastAPI
import subprocess
global host_cache = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '.' in host:
        return {"error": "Invalid host name"}
    if host not in host_cache:
        # Using subprocess.run with list to mitigate command injection
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        host_cache[host] = result.stdout
    return {"status": "completed", "output": host_cache[host]}