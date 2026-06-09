from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_subprocess(command: str) -> bytes:
        args = shlex.split(command)
        return subprocess.check_output(args, stderr=subprocess.STDOUT)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    try:
        output = SafeSubprocess.safe_subprocess(command)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output.decode()}