from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if any(char in host for char in [';', '|', '&']):
            return {'status': 'failed', 'error': 'Invalid characters in host'}
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)