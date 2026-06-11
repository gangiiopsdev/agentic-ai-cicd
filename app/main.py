from fastapi import FastAPI
import subprocess
def execute_command(command):
    return subprocess.call(command, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = execute_command(command)
    return {"status": "completed", "result": result}