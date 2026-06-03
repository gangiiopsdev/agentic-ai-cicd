from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host or ' ' in host or ';' in host or '|' in host or '&' in host:
            raise ValueError('Invalid host')
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)