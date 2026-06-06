from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    args = shlex.split(' '.join(args))
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    args = shlex.split(' '.join(args))
    subprocess.run(args, check=True)
    return {"status": "completed"}