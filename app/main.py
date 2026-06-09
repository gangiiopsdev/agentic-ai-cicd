from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}