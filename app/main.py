from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate host input to prevent injection attacks
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            raise ValueError('Invalid host name')
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)