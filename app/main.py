from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Input validation to prevent command injection
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional recommendation: Consider using a whitelist of allowed hosts or validate the input more strictly.