from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    sanitized_host = host.strip()
    if not sanitized_host:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': e.stderr}

app = FastAPI()
@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get('/ping')
def ping(host: str):