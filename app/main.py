from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = host.replace(';', '').replace('&', '').replace('|', '')  # Basic sanitization
        result = subprocess.run(['ping', '-c', '1'] + [safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

global app
app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.ping(host)