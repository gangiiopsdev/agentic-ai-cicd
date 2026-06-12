from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in '-._' for c in host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    return safe_ping(host)