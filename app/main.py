from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with additional validation
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}