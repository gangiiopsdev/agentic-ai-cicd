from fastapi import FastAPI
import subprocess
cimport os

class SafePing:
    @staticmethod
def safe_ping(host: str) -> bool:
        if not host or ' ' in host:
            print('Invalid host input')
            return False
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error: {e.stderr}')
            return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if SafePing.safe_ping(host):
        return {'status': 'completed', 'result': True}
    else:
        return {'status': 'failed', 'result': False}