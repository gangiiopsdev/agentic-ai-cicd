from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        SafeSubprocess.run(f'ping -c 1 {host}', shell=False)
        return {"status": "completed", "result": "success"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}