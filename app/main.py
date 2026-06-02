from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)