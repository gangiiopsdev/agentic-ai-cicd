from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}