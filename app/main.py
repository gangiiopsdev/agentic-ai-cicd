from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_str):
    return re.sub(r'[^a-zA-Z0-9. ]', '', input_str).strip()

def execute_command(command, *args, **kwargs):
    try:
        output = subprocess.run(command + args, capture_output=True, text=True, check=True, **kwargs)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_command(['ping'], sanitized_host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}