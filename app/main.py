from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize the host input to prevent command injection
        args = ['ping', '127.0.0.1']  # Hardcoded for demonstration; use a whitelist or validation
        result = subprocess.call(args)
        return result

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    # Use a whitelist or validation for the host input
    if host in ['127.0.0.1', '::1']:  # Example whitelist
        return PingService.ping(host)
    else:
        return {'error': 'Invalid host'}, 400