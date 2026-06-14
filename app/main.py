from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_subprocess(command: str, args: list):
    full_command = f'{command} {" ".join(shlex.quote(arg) for arg in args)}'
    subprocess.call(full_command, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    secure_subprocess("ping", [host])
    return {"status": "completed"}