from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host
class SecurePing:
    @staticmethod
def ping(host: str):
        sanitized_host = sanitize_host(host)
        subprocess.run(['ping', sanitized_host], check=True)
app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    SecurePing.ping(host)
    return {'status': 'completed'}