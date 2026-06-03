from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host):
    try:
        args = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    return run_ping(safe_host)