from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '-' not in host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}