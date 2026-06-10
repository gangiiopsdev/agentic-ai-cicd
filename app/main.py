from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout.decode()}
        else:
            return {'status': 'failed', 'output': result.stderr.decode()}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}