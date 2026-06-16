from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        args = list(shlex.split(' '.join(args)) + list(kwargs.values()))
        return subprocess.call(command, *args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    SafeSubprocess.call(['ping', host])
    return {"status": "completed"}