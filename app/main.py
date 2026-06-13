from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input before using it in the command
    if not host or not all(c.isalnum() for c in host):  # Basic validation, may need more complex checks depending on requirements
        return {'error': 'Invalid hostname'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}