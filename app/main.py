from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host.strip() or not host.isalnum():
        return {'status': 'error', 'output': 'Invalid host input'}
    output = SafePing.safe_ping(subprocess.check_output(['echo', host], text=True).strip())
    return {'status': 'completed', 'output': output}