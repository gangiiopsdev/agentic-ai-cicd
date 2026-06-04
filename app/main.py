from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure the host parameter does not contain any malicious input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host):
        return subprocess.run(['ping', host], shell=False, check=True)
    else:
        raise ValueError('Invalid characters in host parameter')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}