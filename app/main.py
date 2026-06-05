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
    if host not in ping_host_set:
        ping_host_set.add(host)
    try:
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}