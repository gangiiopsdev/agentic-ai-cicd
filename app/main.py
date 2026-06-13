from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = ''.join(e for e in host if e.isalnum() or e.isspace())  # Sanitize input
    PingService.ping(sanitized_host)
    return {'status': 'completed'}