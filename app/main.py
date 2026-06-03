from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return {'status': 'failed', 'error': result['error']}
    else:
        return {'status': 'completed', 'output': result['output']}