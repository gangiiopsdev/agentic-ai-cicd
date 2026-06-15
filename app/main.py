from fastapi import FastAPI
import subprocess
def shell_escape(s):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in s)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shell_escape(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}