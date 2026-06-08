from fastapi import FastAPI
import subprocess
global host_to_ping
host_to_ping = '8.8.8.8' # Replace this with a safe default or use a parameterized approach

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str=None):
    if host is None:
        host = host_to_ping
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}