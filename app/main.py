from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using check_output and shell=False
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app.get('/', endpoint=home)
app.get('/ping', endpoint=ping)