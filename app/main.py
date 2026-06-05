from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE, STDOUT

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    p = Popen(['ping', host], stdout=PIPE, stderr=STDOUT)
    output, errors = p.communicate()
    return {'status': 'completed', 'output': output.decode() if output else None}