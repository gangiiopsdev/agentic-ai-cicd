from fastapi import FastAPI
import subprocess
import shlex

global_host_list = ["example.com"]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_host_list:
        # Secure implementation
        subprocess.call(shlex.split(f"ping {host}"), shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Unauthorized'}, 403