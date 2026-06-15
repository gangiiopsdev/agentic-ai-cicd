from fastapi import FastAPI
import subprocess
import shlex
class SafeHostChecker:
    @staticmethod
    def is_valid_host(host):
        return host.isalnum() or '.' in host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not SafeHostChecker.is_valid_host(host):
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}