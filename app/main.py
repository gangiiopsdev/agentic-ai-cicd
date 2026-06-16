from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', shlex.quote(host)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {'status': 'error', 'message': str(error)}
    return {'status': 'completed'}