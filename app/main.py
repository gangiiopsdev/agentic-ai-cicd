from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' for c in host):
        raise ValueError('Invalid host')
    sanitized_host = ''.join(filter(lambda x: x.isalnum() or x in '-_.', host))
    return subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'result': result.stdout}