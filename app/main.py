from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host parameter to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', f'--{host}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'output': result.stdout}