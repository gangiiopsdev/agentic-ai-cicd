from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
    def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid input')
        try:
            result = subprocess.run(['ping', f'127.0.0.1 -c 4 {host}'], check=True, timeout=5, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError('Ping failed') from e
global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    output = global_safe_ping(host)
    return {'status': 'completed', 'output': output}