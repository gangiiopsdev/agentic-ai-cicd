from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: ['ping'] + shlex.split(host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate or sanitize the input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host input')
    result = subprocess.run(generate_ping_command(host), check=True, capture_output=True)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode() if result.stderr else None}