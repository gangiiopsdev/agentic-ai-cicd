from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=10, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}