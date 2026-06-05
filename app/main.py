from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        args = shlex.split(f'ping {safe_host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}