from fastapi import FastAPI
import subprocess
import shlex
import os

ping_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts to allow

global ping_safe_hosts
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ping_safe_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Avoid using shell and use check=True to handle errors
    return {'status': 'completed'}