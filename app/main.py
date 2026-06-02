from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex to safely handle the command arguments
        subprocess.call(['ping', *shlex.split(host)], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400