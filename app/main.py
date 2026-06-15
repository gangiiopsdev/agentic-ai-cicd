from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    try:
        cmd = ['ping'] + shlex.split(host)
        output = subprocess.check_output(cmd, universal_newlines=True, shell=False)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)