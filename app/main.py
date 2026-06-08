from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_check_output(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.check_output(args, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = SafeSubprocess.safe_check_output(f'ping {host}', timeout=5, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}
    except subprocess.TimeoutExpired as e:
        return {'status': 'timeout', 'message': 'Command timed out'}