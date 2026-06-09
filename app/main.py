from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host parameter is sanitized before using in ping command
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}