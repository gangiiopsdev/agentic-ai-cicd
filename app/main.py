from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input to prevent injection
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)