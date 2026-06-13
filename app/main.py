from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if host and isinstance(host, str) and len(host.strip()) > 0:
        subprocess.call(shlex.split("ping {}".format(host)), shell=False)
    return {"status": "completed"}