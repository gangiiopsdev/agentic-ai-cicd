from fastapi import FastAPI
import subprocess
global_vars = {'__builtins__': None}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host], shell=False, env=global_vars)

    return {'status': 'completed'}