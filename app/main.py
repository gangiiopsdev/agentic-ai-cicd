from fastapi import FastAPI
import subprocess
def escape_shell_command(cmd):
    return [arg.replace('`', '\`') for arg in cmd]

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for ping host')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}