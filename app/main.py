from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input
    if not host.strip() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)