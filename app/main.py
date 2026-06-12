from fastapi import FastAPI
import subprocess
cimport os
def execute_command(command: str):
    if not os.path.exists('/bin/' + command.split()[0]):
        raise ValueError('Executable does not exist')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    execute_command(command)
    return {"status": "completed"}