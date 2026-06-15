from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add validation logic here
    return host.strip().endswith('.com')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Safe implementation
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'invalid input'}, 400