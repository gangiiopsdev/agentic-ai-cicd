from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize host input to prevent shell injection
        if not host.strip():
            raise ValueError('Host parameter cannot be empty or contain only whitespace.')
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}