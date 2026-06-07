from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, capture_output=True, check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, capture_output=True, check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}