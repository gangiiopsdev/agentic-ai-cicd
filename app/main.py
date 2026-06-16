from fastapi import FastAPI
import subprocess
import shlex

class ShellCommandError(Exception):
    pass

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(host)
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise ShellCommandError(f'Failed to execute ping command: {e}')