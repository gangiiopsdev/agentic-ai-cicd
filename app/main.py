from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent code injection
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {'error': 'Invalid input'}, 400
    command = generate_ping_command(host)
    subprocess.run(command, shell=False, check=True, capture_output=True)
    return {'status': 'completed'}