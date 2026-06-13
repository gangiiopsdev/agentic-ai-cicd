from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if host.strip() in ['localhost', '127.0.0.1']:
            return subprocess.call(['ping', *shlex.split(host)], shell=False)
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        SafePing.safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400