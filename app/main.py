from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False and args
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}