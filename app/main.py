from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

generate_ping_command = lambda host: f'ping {shlex.quote(host)}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    try:
        subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}