from fastapi import FastAPI
import subprocess
def run_command(command):
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    command = f'ping {host}'  # Removed shlex.quote to avoid unnecessary escaping
    output = run_command(command)
    return {'status': 'completed', 'output': output}