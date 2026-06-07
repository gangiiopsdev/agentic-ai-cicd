from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex.split to safely split the command into a list of arguments
        subprocess.run(shlex.split(f'ping {host}'), check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}