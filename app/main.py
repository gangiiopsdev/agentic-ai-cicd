from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error code {e.returncode}'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}