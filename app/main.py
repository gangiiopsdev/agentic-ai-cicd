from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command: list):
    try:
        result = subprocess.run(command, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'error': 'Command failed with error: {}'.format(e.stderr)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    return run_safe_command(command)