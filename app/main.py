from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app.get('/', summary='Home')(home)
app.get('/ping', summary='Ping Host')(ping)