from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Sanitize the host input to prevent command injection
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        sanitized_host = ''.join(char for char in host if char in allowed_chars)
        subprocess.call(['ping', sanitized_host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing.safe_ping(host)
    return {'status': 'completed'}