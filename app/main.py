from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters or commands
    if any(char in host for char in [';', '|', '&', '`']):
        return {'error': 'Invalid input'}, 400
    command = ['ping', *shlex.split(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}