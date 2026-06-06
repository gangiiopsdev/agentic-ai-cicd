from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command: str, *args):
    full_command = [command] + list(shlex.split(' '.join(args)))
    try:
        output = subprocess.check_output(full_command, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_command('ping', host)