from fastapi import FastAPI
import subprocess
import shlex
global host
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}