from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess32 for better compatibility and more features
    import subprocess32 as subprocess
    if host.startswith('192.168.') or host.startswith('10.'):  # Example of a simple validation
        subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}