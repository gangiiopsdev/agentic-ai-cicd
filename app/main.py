from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if execute_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}