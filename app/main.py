from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    if not host or '||' in host or ';' in host:
        raise ValueError('Invalid host name')
    return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True).stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'invalid_host', 'message': str(e)}