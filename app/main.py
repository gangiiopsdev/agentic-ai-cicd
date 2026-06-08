from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with path validation and input sanitization
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if host in allowed_hosts:
        command = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = command.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    else:
        return {'error': 'Invalid host'}