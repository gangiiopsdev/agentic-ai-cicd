from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {shlex.quote(host)}'
    result = subprocess.run(command, shell=False)
    return {"status": result.returncode}