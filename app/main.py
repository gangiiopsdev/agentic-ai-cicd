from fastapi import FastAPI
import subprocess
def safe_ping(host):
    safe_hosts = ['127.0.0.1']
    if host not in safe_hosts:
        raise ValueError('Invalid input')
    result = subprocess.run(['ping', f'{host}'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)