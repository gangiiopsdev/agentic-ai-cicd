from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.run(args, check=True)
    return {"status": "completed"}