from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}