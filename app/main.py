from fastapi import FastAPI
import subprocess
import shlex

global_host = '127.0.0.1' # Define a safe default value for host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str=global_host):
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {"status": "completed"}