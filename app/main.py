from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str) -> dict:
        safe_host = ''.join(c for c in host if c.isalnum() or c == '.')
        try:
            result = subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not SafePing.is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    return SafePing.ping(host)

class SafePing:
    @staticmethod
def is_safe_host(host: str) -> bool:
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
        return all(char in allowed_chars for char in host)