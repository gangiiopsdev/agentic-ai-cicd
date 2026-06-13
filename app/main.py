from fastapi import FastAPI
import subprocess
def generate_ping_command(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    return ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = subprocess.run(generate_ping_command(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}