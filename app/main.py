from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        args = [arg for arg in args]
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.call(command, *args, **kwargs)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    SafeSubprocess.call(command)

    return {"status": "completed"}