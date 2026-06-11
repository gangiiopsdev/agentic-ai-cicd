from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run_command(command: str, *args):
        parts = shlex.split(command)
        process = subprocess.Popen(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = f'ping {host} -c 4'
    result = SafeSubprocess.run_command(command)
    return result