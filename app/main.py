from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def execute(command: str, *args, **kwargs):
        try:
            output = subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafeSubprocess.execute(f'ping {host}')