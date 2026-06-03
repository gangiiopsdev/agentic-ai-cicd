from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize host input more thoroughly
        host = ''.join(filter(str.isalnum, host))
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    # Ensure host input is sanitized to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)