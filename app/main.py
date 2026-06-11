from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace("'", "\'").replace('"', '\"')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host format')
    escaped_host = escape_shell_arg(host)
    subprocess.call(shlex.split(f'ping {escaped_host}'))
    return {'status': 'completed'}