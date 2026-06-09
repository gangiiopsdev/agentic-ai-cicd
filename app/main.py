from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    cmd = 'ping'
    args = shlex.split(f'{cmd} {host}')
    result = subprocess.run(
        args,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode('utf-8') if not result.stderr else result.stderr.decode('utf-8')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}