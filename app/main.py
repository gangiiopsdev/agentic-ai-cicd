from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

app.get("/home") = home
app.get("/ping") = ping