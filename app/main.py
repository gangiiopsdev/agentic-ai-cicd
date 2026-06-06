from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize host parameter
    if not host.isalnum() or '.' in host:
        return {'status': 'invalid host'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        sanitized_output = ''.join(c for c in result.stdout if c.isprintable())
        return {'status': 'completed', 'output': sanitized_output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}