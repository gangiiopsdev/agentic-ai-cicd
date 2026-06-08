from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    full_command = [' '.join(shlex.split(part)) for part in command_parts]
    try:
        subprocess.run(full_command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_command(['ping', host])