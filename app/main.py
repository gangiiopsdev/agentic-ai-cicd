from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid command injection
    if not host.isalnum() or '@' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}