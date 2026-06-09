from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain any potentially dangerous characters
        if '@' in host or '>' in host or '<' in host or '\' in host or '/' in host or ':' in host or '|' in host or ';' in host or '&' in host or '`' in host or '$' in host or '#' in host or '?' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}