from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    if isinstance(command, list):
        result = subprocess.run(command, capture_output=True, text=True)
    else:
        raise ValueError("Command must be a list")
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    output = run_command(command)
    return {"status": "completed", "output": output}