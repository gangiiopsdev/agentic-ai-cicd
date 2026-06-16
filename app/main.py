from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True)
    return result.stdout.decode()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}