import subprocess
from fastapi import FastAPI
def ping(host: str):
    sanitized_host = host.strip().replace(';', '').replace('&', '')
    # Use an alternative for safe execution
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)