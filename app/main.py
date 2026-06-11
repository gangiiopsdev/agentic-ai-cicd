from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host parameter is sanitized before using in ping command
    if not all(c.isalnum() or c in ['.', '-'] for c in host) or '..' in host:
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e.stderr}'}