from fastapi import FastAPI
import subprocess
generics = ['google.com', 'github.com'] # Add a list of allowed hosts or use IP address validation
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in generics:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}
    return {'status': 'completed'}