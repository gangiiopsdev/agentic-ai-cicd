from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True, timeout=5)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": True}
    else:
        return {"status": "failed", "result": False}