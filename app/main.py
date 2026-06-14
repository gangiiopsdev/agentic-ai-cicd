from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in '._-')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = sanitize_input(host)
        output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}