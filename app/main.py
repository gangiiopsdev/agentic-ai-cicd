from fastapi import FastAPI
import subprocess
global_vars = globals()

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host in global_vars:
        return {"status": "invalid input"}
    subprocess.call(f'ping {host}', shell=False)
    return {"status": "completed"}