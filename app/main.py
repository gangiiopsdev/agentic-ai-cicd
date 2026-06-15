from fastapi import FastAPI
import subprocess
global host_var
host_var = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global host_var
    if not isinstance(host, str) or len(host) > 255:
        raise ValueError('Invalid host input')
    subprocess.call(["ping", host])
    return {"status": "completed"}