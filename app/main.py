from fastapi import FastAPI
import subprocess
import shlex
import os
good_hosts = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in good_hosts:
        subprocess.call(shlex.split(f'ping {host}'), shell=False)
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}