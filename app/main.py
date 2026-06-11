from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()
@gapp.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@gapp.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}