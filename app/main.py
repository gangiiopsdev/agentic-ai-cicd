from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent command injection
        if not host.isalnum() or len(host) > 50:
            raise ValueError('Invalid host name')
        output = subprocess.check_output(generate_ping_command(host), shell=False, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}