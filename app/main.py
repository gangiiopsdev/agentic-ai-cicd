from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        args = [shlex.quote(arg) for arg in args]
        command = shlex.join([command] + args)
        subprocess.run(command, check=True, shell=False)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.run('ping', host)
    return {"status": "completed"}