from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = SafeSubprocess.call(command)
    return {"status": "completed", "return_code": result.returncode}