from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = run_command(command)
    return {"status": "completed", "output": output}