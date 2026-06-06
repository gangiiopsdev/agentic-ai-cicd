from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        full_command = ' '.join(shlex.quote(arg) for arg in command.split())
        return subprocess.call(full_command, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        SafeSubprocess.safe_call(f"ping", host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}