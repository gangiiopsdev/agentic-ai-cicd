from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def execute_command(command: str):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=False)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    if os.path.exists(command.split()[0]):
        return execute_command(command)
    else:
        return {"status": "failed", "error": "Executable not found"}