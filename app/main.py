from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise HTTPException(status_code=400, detail='Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}