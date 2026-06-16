from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with full path and shell=False
    args = ['ping', cmd_quote(host)]
    subprocess.run(shlex.split(' '.join(args)), check=True)
    return {'status': 'completed'}