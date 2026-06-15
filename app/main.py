from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)