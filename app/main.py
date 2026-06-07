from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        # Use subprocess.run with check_output for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic input validation to prevent injection
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)