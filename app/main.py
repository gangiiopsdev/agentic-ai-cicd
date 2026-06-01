from fastapi import FastAPI
import subprocess
cimport = subprocess.run

class SafePing:
    @staticmethod
def ping(host: str):
        try:
            result = cimport(f'ping {host}', capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)