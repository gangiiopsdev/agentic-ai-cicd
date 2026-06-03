from fastapi import FastAPI
import re
import subprocess

def safe_ping(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid input'
    try:
        result = subprocess.run(['ping', '--quiet', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
class PingService:
    @staticmethod
def ping(host: str) -> dict:
        status = 'completed' if safe_ping(host) != 'Invalid input' else 'failed'
        output = {'status': status, 'output': safe_ping(host)} if status == 'completed' else {'status': status, 'error': safe_ping(host)}

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_endpoint(host: str):
    return PingService.ping(host)