from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char.isspace())
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', *shlex.split(sanitized_host)]
    try:
        process = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output = process.stdout.decode()
        error = process.stderr.decode() if process.stderr else None
        return {'status': 'completed', 'output': output, 'error': error}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.output.decode(), 'error': e.stderr.decode()}