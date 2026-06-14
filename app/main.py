from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '._-' else f'\{ord(c):03o}' for c in arg)

def safe_ping(host: str):
    escaped_host = escape_shell_arg(host)
    args = shlex.split(f'ping {escaped_host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}