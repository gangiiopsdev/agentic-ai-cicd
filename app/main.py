from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    # Sanitize the command before execution
    sanitized_args = [arg.encode().decode() for arg in args]
    result = subprocess.run(sanitized_args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}