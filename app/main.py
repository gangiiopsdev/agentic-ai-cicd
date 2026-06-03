from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Secure implementation with shell=False and using shlex.quote for safe argument passing
        subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)