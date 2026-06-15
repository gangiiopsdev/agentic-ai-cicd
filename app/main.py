from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Basic input sanitization (e.g., removing special characters)
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit() or e.isspace())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}