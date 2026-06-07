from fastapi import FastAPI
import subprocess
cimport shlex
def execute_ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}