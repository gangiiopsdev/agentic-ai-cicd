from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run_secure_command(command: str):
        args = shlex.split(command)
        subprocess.run(args, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    run_secure_command(f'ping {shlex.quote(host)}')
    return {'status': 'completed'}