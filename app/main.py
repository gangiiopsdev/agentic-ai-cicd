from fastapi import FastAPI
import subprocess as sp
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host or not host.strip() or '@' in host:
        return {'error': 'Invalid host parameter'}
    args = ['ping', host]
    result = sp.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}