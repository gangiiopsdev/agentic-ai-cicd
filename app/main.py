from fastapi import FastAPI
import subprocess
c
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_endpoint(host: str):
    if '@' not in host and len(host) < 256:
        return ping(host)
    else:
        return {'error': 'Invalid host'}, 400