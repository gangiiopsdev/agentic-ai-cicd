from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str) -> dict:
        safe_host = ''.join(c for c in host if c.isalnum() or c in '.-_')
        try:
            result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return SafePing.ping(host)