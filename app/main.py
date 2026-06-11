from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ['.', '-'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(['ping', safe_host])
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}
    return {'status': 'completed'}