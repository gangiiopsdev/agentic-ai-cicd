from fastapi import FastAPI
import subprocess
cimport os
cimport shutil
cimport tempfile

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to avoid command injection
    if not host or len(host) > 256:
        return {'error': 'Invalid host input'}
    command = ['ping', host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}