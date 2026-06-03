from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate host to prevent injection attacks
        if not host.isalnum() or '.' not in host:
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}