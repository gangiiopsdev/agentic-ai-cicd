from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

def validate_host(host: str) -> bool:
    return bool(host.strip()) and host.isalnum()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host input'}
    output = SafePing.safe_ping(subprocess.check_output(['echo', host], text=True).strip())
    return {'status': 'completed', 'output': output}