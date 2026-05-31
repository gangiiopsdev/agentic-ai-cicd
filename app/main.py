from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {"status": "completed"}