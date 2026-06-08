from fastapi import FastAPI
import subprocess
global_popen = subprocess.Popen,

def safe_subprocess_call(command):
    global_popen(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_subprocess_call(f'ping {host}')

    return {"status": "completed"}