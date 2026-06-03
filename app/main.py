from fastapi import FastAPI
import subprocess
import shlex
def execute_safe_command(command, *args):
    safe_args = [shlex.quote(arg) for arg in args]
    subprocess.run([command] + safe_args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_command('ping', host)
    return {"status": "completed"}