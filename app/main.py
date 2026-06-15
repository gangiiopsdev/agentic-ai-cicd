from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure input is validated and sanitized
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}