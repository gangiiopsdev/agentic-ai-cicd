from fastapi import FastAPI
import subprocess
import shlex

gapp = FastAPI()

@gapp.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@gapp.get("/ping")
def ping(host: str):
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}