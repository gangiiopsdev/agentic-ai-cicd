from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = shlex.split(f'ping {shlex.quote(host)}')
    try:
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}