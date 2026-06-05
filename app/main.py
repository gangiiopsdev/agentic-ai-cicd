from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

global_env = {}  # Ensure all environment variables are safe

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split('ping -c 1 {}'.format(host))
        subprocess.run(args, check=True, env=global_env)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}