from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: ['ping', shlex.quote(host)]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    process = subprocess.run(generate_ping_command(host), check=True, capture_output=True)
    return {
        'status': 'completed',
        'stdout': process.stdout.decode(),
        'stderr': process.stderr.decode() if process.stderr else None
    }