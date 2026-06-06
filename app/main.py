from fastapi import FastAPI
import subprocess
import shlex
import os

def secure_ping(host: str):
    escaped_host = shlex.quote(host)
    command = ['ping', escaped_host]
    subprocess.run(command, check=True, shell=False)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}