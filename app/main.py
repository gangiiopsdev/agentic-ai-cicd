from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def check_output(command, host):
        safe_command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(safe_command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = SafeSubprocess.check_output('ping', host)
        return result
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}