from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        if host and all(c.isalnum() or c in ('.', '-') for c in host):
            try:
                output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
                return {'status': 'completed', 'output': output.decode()}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': e.output.decode()}
        else:
            return {'status': 'failed', 'error': 'Invalid host name'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)