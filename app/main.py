from fastapi import FastAPI
import subprocess
cimport shlex

gapp = FastAPI()

@gapp.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.Popen
    args = shlex.split(f"ping {host}")
    subprocess.Popen(args)
    return {"status": "completed"}