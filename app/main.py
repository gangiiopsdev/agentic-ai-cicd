from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    # Use subprocess.run instead of subprocess.call for better security and control over the output
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}