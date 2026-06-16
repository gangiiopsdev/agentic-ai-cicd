from fastapi import FastAPI
import subprocess
import shlex


def safe_ping(host):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': 'Invalid input'}