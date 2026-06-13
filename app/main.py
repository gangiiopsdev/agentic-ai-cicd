from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host or any(char in host for char in [';', '|', '&', '<', '>', '*', '?', '~', '`', '$', '\', '{', '}', '[', ']', ':', '/', '\\', '#']):
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation using subprocess.run with shell=False and list of arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}