from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host in allowed_hosts:
        return subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    else:
        raise ValueError('Host not allowed')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}