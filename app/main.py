from fastapi import FastAPI
import subprocess
import shlex
import os
global ping_safe_hosts
ping_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts to allow

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ping_safe_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], shell=False)  # Use subprocess.run for better control and security
    return {'status': 'completed'}