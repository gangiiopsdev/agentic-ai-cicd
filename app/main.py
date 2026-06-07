from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Basic sanitization example
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', ' ', ':'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}