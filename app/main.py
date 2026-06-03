from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Using subprocess.run for safer execution
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}