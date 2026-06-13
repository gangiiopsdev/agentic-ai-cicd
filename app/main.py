from fastapi import FastAPI
import subprocess
global_params = {"ping": "-c 1", "traceroute": "-m 5"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    if host in global_params:
        subprocess.call(["ping", *global_params[host].split()], shell=False)
    else:
        return {"error": "Invalid host parameter"}

    return {"status": "completed"}