from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.replace('.', '').isnumeric() or '@' in host:
        raise ValueError('Invalid host format')
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)