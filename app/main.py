from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs) -> None:
        args = [command] + list(args)
        full_command = shlex.split(' '.join(args))
        subprocess.call(full_command, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.call(f'ping {host}')
    return {"status": "completed"}