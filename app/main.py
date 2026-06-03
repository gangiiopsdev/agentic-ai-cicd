from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize the host input to prevent command injection
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ('-', '.', '_', ':'))
        command = ['ping', sanitized_host]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        output = SafePing.ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}