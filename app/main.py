from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation
    if host and all(c in string.ascii_letters + '.' for c in host):
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid hostname')