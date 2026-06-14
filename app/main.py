from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def sanitize_input(input_str):
    if ' ' in input_str or '>' in input_str or '<' in input_str:
        raise ValueError('Invalid input')
    return input_str
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    return execute_ping(host)