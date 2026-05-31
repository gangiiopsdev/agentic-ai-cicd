from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ['ping', host]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        command = generate_ping_command(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}