from fastapi import FastAPI
import subprocess

app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Further secure implementation
    if not host.isalnum() or '@' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}