from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', subprocess.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)