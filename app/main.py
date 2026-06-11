from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(str(arg))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {escape_shell_arg(host)}')
    subprocess.call(args)
    return {'status': 'completed'}