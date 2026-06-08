from fastapi import FastAPI
import subprocess
global host_blacklist = set(['127.0.0.1', 'localhost'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in host_blacklist and '.' in host:
        # Use subprocess.run instead of subprocess.call for better security control
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Host is blacklisted or invalid')