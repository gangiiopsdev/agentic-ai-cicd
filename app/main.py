from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent shell injection
    if not all(c.isalnum() or c in '-.' for c in host) or '..' in host:
        raise ValueError('Invalid hostname')
    result = SafeSubprocess.safe_ping(host)
    return {'status': 'completed', 'result': result}