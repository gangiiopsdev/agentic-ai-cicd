from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.split
    import shlex
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run and shlex.split
    import shlex
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}