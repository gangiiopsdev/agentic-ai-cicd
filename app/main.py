from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['.', '-', '_'])
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}