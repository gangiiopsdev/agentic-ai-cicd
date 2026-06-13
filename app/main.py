from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}