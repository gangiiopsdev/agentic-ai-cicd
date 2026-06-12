from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using Popen and check_output
        result = subprocess.check_output(['ping', host], shell=False, timeout=5)
        return {'status': 'completed', 'result': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping request timed out'}