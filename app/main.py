from fastapi import FastAPI
import subprocess

def generate_command(host: str):
    # Validate host input
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host name')
    return ['ping', host]

generate_command = lambda host: generate_command(host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(generate_command(host), shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}