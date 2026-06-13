from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in ('.', '_', '-'))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}