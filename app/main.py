from fastapi import FastAPI
import subprocess
def secure_ping(host):
    # Validate host to ensure it's a trusted source
    if not host.isalnum():
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = secure_ping(host)
    return {'status': 'completed', 'output': output}