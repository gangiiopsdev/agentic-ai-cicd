from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(ch for ch in host if ch.isalnum() or ch in ('-', '.', '_', ':'))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping', sanitized_host]
    subprocess.call(command)
    return {'status': 'completed'}