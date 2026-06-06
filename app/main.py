from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Use subprocess.run for safer execution with proper argument passing
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input before passing to safe_ping
    if not host.strip().replace('.', '').isdigit() or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    try:
        SafePing.safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500
    return {'status': 'completed'}