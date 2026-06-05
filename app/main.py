from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess_command(command, *args):
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not host or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid host'}
    safe_host = subprocess.list2cmdline([host])
    result = safe_subprocess_command('ping', *safe_host.split())
    return {'status': 'completed', 'output': result.stdout}