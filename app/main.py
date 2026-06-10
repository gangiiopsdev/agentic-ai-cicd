from fastapi import FastAPI
import subprocess
global_ping_command = 'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(global_ping_command.format(host=host), shell=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}