from fastapi import FastAPI
import subprocess
import shlex
global host_list
host_list = ["127.0.0.1", "8.8.8.8"]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if host in host_list:
        args = shlex.split(f"ping {host}")
        subprocess.call(args, shell=False)
    else:
        return {"error": "Unauthorized host"}
    return {"status": "completed"}