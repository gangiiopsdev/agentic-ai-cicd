from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using check_output with safe command construction
        args = ['ping', '-c', '1'] + shlex.split(host)
        subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'message': f'Ping to {host} successful'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}