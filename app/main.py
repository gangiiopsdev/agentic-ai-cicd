from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent command injection
    if not host.strip().isalnum():
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)