from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def escape_command(input_str):
    return ' '.join(shell_quote(arg) for arg in input_str.split())

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_command(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, shell=False)
    return {'status': 'completed'}