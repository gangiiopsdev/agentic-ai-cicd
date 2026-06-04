from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum())

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = _sanitize_input(host)
    result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}