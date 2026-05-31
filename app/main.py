from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using check_output with shell=False
    try:
        result = subprocess.check_output(['ping', '-c', '1', host], timeout=5)
        return {'status': 'completed', 'result': result.decode('utf-8')}
    except (subprocess.CalledProcessError, TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}