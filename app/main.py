from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    generate_ping_command = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': generate_ping_command.stdout}

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_host(host: str):
    result = ping(host)
    return result