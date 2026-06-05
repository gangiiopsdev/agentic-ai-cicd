from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    args = command.split()
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_command(f'ping {host}')
    return {"status": "completed"}