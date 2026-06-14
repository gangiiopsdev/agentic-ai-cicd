from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and '-' not in host:
        return {'status': 'error', 'error': 'Invalid host name'}
    return ping(host)