from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run([quote(arg) for arg in command], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", quote(host)]
    output = run_command(command)
    return {"status": "completed", "output": output}