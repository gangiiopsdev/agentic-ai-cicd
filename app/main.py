from fastapi import FastAPI
import subprocess
def escape_host(host):
    # More comprehensive escaping to prevent shell injection
    return ''.join(c for c in host if c.isalnum() or c in ('-', '_', '.', ':'))

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with more comprehensive input escaping and proper subprocess usage
    try:
        result = subprocess.run(['ping', escape_host(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}