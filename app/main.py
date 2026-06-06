from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Enhanced input validation
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    # Use ping3 for safer and more flexible pinging
    from ping3 import ping
    response = ping(host)
    if response is None:
        raise ValueError('Ping failed')
    return response

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    safe_ping(host)
    return {'status': 'completed', 'response': 'success'}