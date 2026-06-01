from fastapi import FastAPI
import subprocess
import shlex
import os

class SafeSubprocess:
    @staticmethod
    def safe_exec(command: str, args: list) -> bytes:
        command = shlex.quote(command)
        for arg in args:
            arg = shlex.quote(arg)
        return subprocess.check_output([command] + args, timeout=5, stderr=subprocess.STDOUT)

global_safe_subprocess = SafeSubprocess()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        output = global_safe_subprocess.safe_exec('ping', ['-c', '1', host])
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}