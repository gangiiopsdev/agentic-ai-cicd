from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        args = ['ping', host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

def safe_ping(host):
    return SafePing.run(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}