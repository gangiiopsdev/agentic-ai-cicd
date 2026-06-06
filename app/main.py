from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_safe_command(command: str, *args):
    safe_args = [shlex.quote(arg) for arg in args]
    full_command = [command] + safe_args
    try:
        output = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    try:
        output = run_safe_command('ping', host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)