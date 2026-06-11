from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize and validate the host parameter more thoroughly
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1'] + shlex.split(host)  # Use shlex to safely split the host parameter
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return {'status': 'failed', 'error': result['error']}
    else:
        return {'status': 'completed', 'output': result['output']}