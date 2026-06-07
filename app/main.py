from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host: str) -> dict:
        if '&&' in host or ';' in host or '|' in host or '`' in host:
            return {'status': 'failed', 'error': 'Invalid characters in input'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.run(host)