from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '.-')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}