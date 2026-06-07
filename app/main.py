from fastapi import FastAPI
import subprocess

def execute_command(command):
    return subprocess.run(command, capture_output=True, text=True)

def safe_execute_command(host):
    command = ['ping', host.strip()]
    return execute_command(command)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_execute_command(host)
    return {'status': 'completed', 'output': result.stdout}