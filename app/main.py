from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simple validation
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout,

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed'}
    return {'status': 'completed', 'output': output}