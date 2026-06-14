from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, params):
    return subprocess.run(command + list(params), capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result = execute_command(command, [])
    return {"status": "completed", "output": result.stdout.decode() if not result.stderr else result.stderr.decode()}