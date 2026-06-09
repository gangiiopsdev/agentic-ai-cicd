from fastapi import FastAPI
import subprocess
def escape_shell_command(command: str) -> str:
    return subprocess.list2cmdline(command.split())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(escape_shell_command(f'ping {host}'))
    return {'status': 'completed'}