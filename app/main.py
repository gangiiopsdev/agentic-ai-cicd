from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and validation of host input
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):  # Basic validation
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}