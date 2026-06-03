from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = [shlex.split(arg) for arg in args]
        return subprocess.run([command] + list(args), check=True, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.call(f'ping', host)

    return {"status": "completed"}