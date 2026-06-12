from fastapi import FastAPI
import subprocess
import shlex

global ping_host_list
ping_host_list = ["8.8.8.8", "127.0.0.1"]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ping_host_list:
        raise HTTPException(status_code=403, detail="Invalid host")

    # Safe implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {"status": "completed"}