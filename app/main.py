from fastapi import FastAPI
import subprocess
import shlex

global pinger

app = FastAPI()

def ping_command(host):
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = ping_command(host)
    return {"status": "completed", "output": result}