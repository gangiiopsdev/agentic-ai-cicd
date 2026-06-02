from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app.get('/', endpoint=home)
app.get('/ping', endpoint=ping)