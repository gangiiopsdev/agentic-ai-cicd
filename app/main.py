from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_check_output(command: str, **kwargs):
        args = shlex.split(command)
        return subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        command = f'ping {shlex.quote(host)}'
        output = SafeSubprocess.safe_check_output(command)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}