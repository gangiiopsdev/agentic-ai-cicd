from fastapi import FastAPI
import re
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command, args):
        if not isinstance(args, list) or not all(isinstance(arg, str) for arg in args):
            raise ValueError("Invalid arguments")
        command = subprocess.list2cmdline([command])
        args = [subprocess.list2cmdline([arg]) for arg in args]
        try:
            result = subprocess.run([command] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
            return {'status': 'completed', 'result': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()} 

app = FastAPI()
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '-_.')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', '-c', '1', sanitized_host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return {'status': 'completed', 'result': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}