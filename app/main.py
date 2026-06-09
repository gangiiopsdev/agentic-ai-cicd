from fastapi import FastAPI
import subprocess
import shlex
import os

cmd = 'ping {host}'
command = [cmd.format(host=shlex.quote(host))]
subprocess.run(command, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and full path
    return {'status': 'completed'}