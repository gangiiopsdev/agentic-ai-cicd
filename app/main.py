from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess_call(command: list) -> int:
    return subprocess.call(shlex.split(' '.join(command)))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess_result = safe_subprocess_call(command)
    return {'status': 'completed', 'subprocess_result': subprocess_result}