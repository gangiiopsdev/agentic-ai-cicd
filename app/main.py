from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation of host to prevent common injection issues
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid hostname')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        # Use subprocess.run with shell=False and arguments properly escaped to prevent command injection
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}