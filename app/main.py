from fastapi import FastAPI
import subprocess
import shlex
global_host = 'example.com'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host == global_host:
        safe_command = shlex.split(f'ping {host}')
        try:
            result = subprocess.run(safe_command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Unauthorized access attempt'}