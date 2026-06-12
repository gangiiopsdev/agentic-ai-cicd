from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command, *args):
    full_command = [command] + list(shlex.split(' '.join(args)))
    result = subprocess.run(full_command, check=True)
    return result

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper argument handling
    safe_subprocess('ping', host)
    return {'status': 'completed'}