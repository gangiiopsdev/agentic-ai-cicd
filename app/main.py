from fastapi import FastAPI
import subprocess
global ping_host_set
ping_host_set = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_host_set
    if host in ping_host_set:
        return {"error": "Host already pinging"}
    ping_host_set.add(host)
    result = subprocess.call(['ping', '-c', '1', host], capture_output=True, text=True)
    ping_host_set.remove(host)
    return {"status": "completed", "result": result.stdout}