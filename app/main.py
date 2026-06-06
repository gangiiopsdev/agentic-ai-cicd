from fastapi import FastAPI
import subprocess
cimport socketio

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use socketio to check connectivity instead of shell command
        sio = socketio.Client()
        sio.connect(f'http://{host}')
        return {'status': 'completed', 'message': f'Successfully connected to {host}'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}