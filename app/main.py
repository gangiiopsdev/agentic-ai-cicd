from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c.isdigit() or c in ['.', '-', '_'] for c in host):
        raise ValueError('Invalid host name')
    return ['ping', '-c', '4', host]
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        command = generate_ping_command(host)
        result = subprocess.run(command, capture_output=True, text=True, shell=False, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}