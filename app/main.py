from fastapi import FastAPI
import re

def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
ping