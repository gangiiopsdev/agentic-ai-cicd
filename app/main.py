from fastapi import FastAPI
import subprocess
import shlex
def execute_safe_command(command_args):
    try:
        result = subprocess.run(['ping'] + shlex.split(command_args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.returncode}\nStderr: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.strip().isdigit():  # Validate that the input contains only digits (simple check)
        return {'error': 'Invalid input. Only numeric values are allowed.'}
    result = execute_safe_command(host)
    return {'status': 'completed', 'result': result}