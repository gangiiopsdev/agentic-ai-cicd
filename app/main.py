from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using list for the command arguments
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}