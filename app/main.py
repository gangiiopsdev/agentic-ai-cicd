from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        sanitized_host = subprocess.quote(host)
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric():  # Add validation to ensure the input is numeric (example check)
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_ping(host)