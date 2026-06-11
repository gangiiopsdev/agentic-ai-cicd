from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        try:
            args = ['ping'] + shlex.split(host)
            subprocess.call(args, shell=False)
        except Exception as e:
            return {'error': str(e), 'status': 'failed'}
        return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return PingService.ping(host)