from fastapi import FastAPI
import subprocess
genesis_cmd = ['ping']

app = FastAPI()

def is_valid_host(host):
    return host.isalnum() and '.' in host

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "output": "Invalid host"}
    try:
        result = subprocess.run(genesis_cmd + [host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "output": str(e)}
    return {"status": "completed", "output": result.stdout}