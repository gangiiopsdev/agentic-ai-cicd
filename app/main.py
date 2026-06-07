from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it is a valid hostname or IP address
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}