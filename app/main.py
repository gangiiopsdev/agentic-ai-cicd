from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.replace('-', '').replace('.', '').isalnum():
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        status = SafePing.safe_ping(host)
        return {'status': 'completed', 'output': status}
    except ValueError as e:
        return {'error': str(e)}