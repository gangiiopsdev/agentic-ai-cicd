from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)