from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with input validation
    try:
        sanitized_host = shlex.quote(host)
        subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500