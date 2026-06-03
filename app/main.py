from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}