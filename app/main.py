from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)