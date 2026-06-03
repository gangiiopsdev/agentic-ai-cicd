from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)