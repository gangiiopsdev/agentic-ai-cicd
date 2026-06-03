from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or '..' in host:
        return {'status': 'error', 'output': 'Invalid hostname'}
    result = PingService.ping(host)
    return {'status': 'completed', 'output': result}