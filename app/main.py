from fastapi import FastAPI
import subprocess
cimport ipaddress

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ipaddress.ip_address(host)
        # Safe implementation using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError:
        return {'status': 'Invalid IP address'}