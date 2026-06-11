from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    try:
        SafeSubprocess.call(command)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode()}}