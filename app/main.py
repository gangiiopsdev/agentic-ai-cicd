from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}