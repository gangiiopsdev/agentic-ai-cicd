from fastapi import FastAPI
import subprocess
import shlex
global_params = {'host': ''}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global_params['host'] = host
    # Safe implementation with shlex for argument splitting
    args = ['ping', *shlex.split(global_params['host'])]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}