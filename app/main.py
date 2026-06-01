from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
global ping_service
ping_service = PingService()
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input to prevent command injection
        host = ''.join(c for c in host if c.isalnum() or c in '.-_')
        return ping_service.ping(host)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}