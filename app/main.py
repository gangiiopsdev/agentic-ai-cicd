from fastapi import FastAPI
import subprocess
import shlex

class SafePinger:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4', '--']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    command = SafePinger.ping_command + [safe_host]
    subprocess.call(command)
    return {"status": "completed"}