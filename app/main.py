from fastapi import FastAPI
import subprocess
def execute_command(command: str, args: list) -> dict:
    try:
        result = subprocess.run([command] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    return execute_command('ping', [host])