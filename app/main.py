from fastapi import FastAPI
import subprocess
import shlex

global_vars = globals()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}