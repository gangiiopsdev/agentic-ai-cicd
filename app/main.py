from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '{host}']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() and '_' not in host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        subprocess.run(generate_ping_command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}