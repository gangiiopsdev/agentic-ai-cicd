from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

global_ping_command = 'ping'

@app.get('/ping')
def ping(host: str):
    try:
        args = [global_ping_command, '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}