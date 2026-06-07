from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using check_output to avoid shell=True and prevent command injection
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', host]
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)