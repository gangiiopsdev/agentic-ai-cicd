from fastapi import FastAPI
import subprocess
generics = ('ping',)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.Popen with shell=False and sanitized input
    if host not in generics:
        return {'error': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}