from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.call(args, timeout=1)  # Limit the time to avoid DoS attacks

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.call(f'ping -c 1 {host}')  # Limit the number of pings and specify the interface if necessary
    return {"status": "completed"}