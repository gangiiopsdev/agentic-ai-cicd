from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    try:
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = run_command(command)
    if output:
        return {"status": "completed", "output": output}
    else:
        return {"status": "timeout"}