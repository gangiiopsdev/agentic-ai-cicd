from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with args instead of shell=True
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode()}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Add input validation to prevent command injection
        return {'status': 'error', 'response': 'Invalid input'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}