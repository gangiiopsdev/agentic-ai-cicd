from fastapi import FastAPI
import subprocess
global_config = {'host': 'default_host'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host == global_config['host']:
        subprocess.call(f"ping {host}", shell=False)
    else:
        return {"status": "Access denied"}
    return {"status": "completed"}