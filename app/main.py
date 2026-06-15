from fastapi import FastAPI
import subprocess
g import ipaddress

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate IP address format
        ipaddress.ip_address(host)
        subprocess.call(['ping', host])
    except ValueError:
        return {'error': 'Invalid IP address'}, 400

    return {'status': 'completed'}