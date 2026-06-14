from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command: str):
    try:
        result = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed with error: {e.stderr}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    result = run_command(' '.join(command))
    return {'status': 'completed', 'output': result}