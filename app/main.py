from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.strip():
        return {'error': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

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