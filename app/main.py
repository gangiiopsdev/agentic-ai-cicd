from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid host'}
        command = ['ping', '-c', '1', shlex.quote(host)]  # Use shlex.quote to sanitize the host input
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)