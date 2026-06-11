from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    if host == 'localhost' or host.startswith('192.168.'):
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
    else:
        return {'status': 'failed', 'error': 'Unauthorized host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}