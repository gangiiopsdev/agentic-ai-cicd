from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}