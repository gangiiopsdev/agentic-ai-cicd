from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):  # Enhanced sanitization
            return {'status': 'error', 'output': 'Invalid input'}
        result = subprocess.run(['ping', '-c', '1'] + [host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
global app
app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.ping(host)